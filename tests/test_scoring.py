from app.scoring import score, Weights, _price_feature, _recency_feature
from app.diversity import diversify


def _row(id: str, kind: str, price: float, rating: float, tags, days_old=0.0) -> dict:
    return {"id": id, "kind": kind, "price_per_night": price,
            "rating": rating, "tags": tags, "days_old": days_old}


def test_price_feature_is_normalized() -> None:
    assert _price_feature(0.0, 200.0) == 1.0        # free → best
    assert _price_feature(200.0, 200.0) == 0.0      # at ceiling → worst
    assert 0.0 < _price_feature(100.0, 200.0) < 1.0


def test_recency_halves_at_half_life() -> None:
    fresh = _recency_feature(0.0, half_life=30.0)
    aged = _recency_feature(30.0, half_life=30.0)
    assert fresh == 1.0
    assert abs(aged - 0.5) < 1e-9                    # exactly half at one half-life


def test_tag_match_raises_score() -> None:
    w = Weights()
    matched = _row("a", "hotel", 100.0, 4.0, ["beach"])
    plain = _row("b", "hotel", 100.0, 4.0, [])
    assert score(matched, {"beach"}, 200.0, w) > score(plain, {"beach"}, 200.0, w)


def test_diversify_caps_per_kind() -> None:
    rows = [_row(str(i), "hotel", 100.0, 5.0 - i * 0.1, []) for i in range(5)]
    out = diversify(rows, per_kind_cap=2, limit=10)
    hotels = [r for r in out if r["kind"] == "hotel"]
    assert len(hotels) == 5                          # backfilled: all-hotel catalog
    assert out[0]["id"] == "0"                        # best-first preserved
