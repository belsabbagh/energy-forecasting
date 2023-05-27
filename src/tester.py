from sklearn.metrics import mean_squared_error, mean_absolute_error


def evaluate_model(model, df):
    results = {"mse": {}, "rmse": {}, "mae": {}}
    for column in df.columns:
        series = df[column]
        model.fit(series, series, epochs=200, verbose=0)
        y_pred = model.predict(series, verbose=0)
        results["mse"].update({column: mean_squared_error(series, y_pred)})
        results["rmse"].update(
            {column: mean_squared_error(series, y_pred, squared=False)}
        )
        results["mae"].update({column: mean_absolute_error(series, y_pred)})

    return results


def evaluate_multi_feature_model(model, df):
    results = {"mse": [], "rmse": [], "mae": []}
    model.fit(df, df, epochs=200, verbose=0)
    y_pred = model.predict(df, verbose=0)
    results["mse"].append(mean_squared_error(df, y_pred))
    results["rmse"].append(mean_squared_error(df, y_pred, squared=False))
    results["mae"].append(mean_absolute_error(df, y_pred))
    return results
