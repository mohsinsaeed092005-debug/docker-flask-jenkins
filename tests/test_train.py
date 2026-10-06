from train import load_data, train, predict, evaluate


def test_data_is_reproducible():
    # same seed = same data (reproducibility)
    assert load_data(seed=42) == load_data(seed=42)


def test_model_learns_pattern():
    model = train(load_data())
    assert abs(model["w"] - 2) < 0.2
    assert abs(model["b"] - 1) < 0.5


def test_model_quality():
    data = load_data()
    model = train(data[:80])
    assert evaluate(model, data[80:]) < 1.0


def test_prediction():
    model = train(load_data())
    assert abs(predict(model, 5) - 11) < 0.5
