from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from dvclive import Live

RANDOM_SEED = 42


def main():
    data_dir = Path(__file__).parents[1] / 'data'
    df = pd.read_csv(data_dir / 'orig' / 'winequality-red.csv', sep=';')

    X = df.drop('quality', axis=1).copy()
    y = df['quality'].copy()

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=RANDOM_SEED,
    )

    with Live() as live:
        model = RandomForestRegressor(random_state=RANDOM_SEED)
        model.fit(X_train, y_train)
        score = model.score(X_test, y_test)
        score = np.sqrt(score)
        print(f'RMSE: {score:.4f}')
        live.log_metric('accuracy', score)


if __name__ == '__main__':
    main()
