-- The catalog: one row per bookable stay.
CREATE TABLE listings (
    id            TEXT PRIMARY KEY,
    city          TEXT        NOT NULL,
    kind          TEXT        NOT NULL,
    price_per_night NUMERIC(8,2) NOT NULL,
    rating        REAL        NOT NULL,
    tags          TEXT[]      NOT NULL DEFAULT '{}'
);

-- Searches almost always filter by city + price, so index that pair.
CREATE INDEX idx_listings_city_price ON listings (city, price_per_night);

-- GIN index lets us match tags fast with the && (overlap) operator.
CREATE INDEX idx_listings_tags ON listings USING GIN (tags);

-- Every view/click/booking a user performs — the personalization signal.
CREATE TABLE interactions (
    user_id    TEXT NOT NULL,
    listing_id TEXT NOT NULL REFERENCES listings(id),
    action     TEXT NOT NULL,         -- 'view' | 'click' | 'book'
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_interactions_user ON interactions (user_id, created_at DESC);
