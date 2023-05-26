from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error


def evaluate_model(model, df):
    results = {"mse": {}, "rmse": {}}
    for column in df.columns:
        series = df[column]
        model.fit(series, series, epochs=200, verbose=0)
        y_pred = model.predict(series, verbose=0)
        results["mse"].update({column: mean_squared_error(series, y_pred)})
        results["rmse"].update(
            {column: mean_squared_error(series, y_pred, squared=False)}
        )
    return results


def evaluate_multi_feature_model(model, df):
    results = {"mse": [], "rmse": []}
    model.fit(df, df, epochs=200, verbose=0)
    y_pred = model.predict(df, verbose=0)
    results["mse"].append(mean_squared_error(df, y_pred))
    results["rmse"].append(mean_squared_error(df, y_pred, squared=False))
    return results
