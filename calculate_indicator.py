import pandas as pd


def calculate_ema_signal(df, ema_length=300):
    """
    Calculates buy or sell signals based on EMA criteria.

    :param df: DataFrame containing stock price data.
    :param ema_length: Length of the EMA. Default is 300.
    :return: Tuple (buy_signal, sell_signal) indicating whether there are buy or sell signals.
    """
    df['EMA'] = df['Close'].ewm(span=ema_length, adjust=False).mean()
    # Define buy and sell signals
    buy_signal = (df['Low'] > df['EMA']) & (
            df['Low'].shift(1) <= df['EMA'].shift(1))
    sell_signal = (df['High'] < df['EMA']) & (
            df['High'].shift(1) >= df['EMA'].shift(1))
    return buy_signal.iloc[-1], sell_signal.iloc[-1]


def calculate_rsi(df, period=14):
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))

    df['RSI'] = rsi
    return df


def calculate_ema(df, period=9):
    ema = df['Close'].ewm(span=period, adjust=False).mean()
    return ema


def calculate_heikin_ashi(df):
    ha_df = pd.DataFrame(index=df.index)
    ha_df['HA_Close'] = (df['Open'] + df['High'] + df['Low'] + df['Close']) / 4
    ha_df['HA_Open'] = 0.0
    ha_df['HA_High'] = 0.0
    ha_df['HA_Low'] = 0.0
    for i in range(len(df)):
        ha_df['HA_Open'].iloc[i] = ((df['Open'].iloc[i - 1] + df['Close'].iloc[
            i - 1]) / 2) if i > 0 else (df['Open'].iloc[0] + df['Close'].iloc[
            0]) / 2
        ha_df['HA_High'].iloc[i] = max(df['High'].iloc[i],
                                       ha_df['HA_Open'].iloc[i],
                                       ha_df['HA_Close'].iloc[i])
        ha_df['HA_Low'].iloc[i] = min(df['Low'].iloc[i],
                                      ha_df['HA_Open'].iloc[i],
                                      ha_df['HA_Close'].iloc[i])
    return ha_df


def calculate_bollinger_bands(df, period=20, num_std_dev=2):
    """Calculate Bollinger Bands for a given DataFrame."""
    rolling_mean = df['Close'].rolling(window=period).mean()
    rolling_std = df['Close'].rolling(window=period).std()

    upper_band = rolling_mean + (rolling_std * num_std_dev)
    lower_band = rolling_mean - (rolling_std * num_std_dev)

    df['Bollinger_Upper'] = upper_band
    df['Bollinger_Lower'] = lower_band
    df['Bollinger_Middle'] = rolling_mean

    return df


def buy_signal_bollinger_rsi(df):
    last_row = df.iloc[-1]
    if last_row['Close'] < last_row['Bollinger_Lower'] and last_row[
        'RSI'] > 30:
        stop_loss = last_row['Bollinger_Lower'] * 0.97
        target_price = last_row['Bollinger_Upper']
        # Define entry point range as from the lower Bollinger Band up to 2% above it
        entry_point_start = last_row['Bollinger_Lower']
        entry_point_end = last_row['Bollinger_Lower'] * 1.02
        return True, stop_loss, target_price, (
            entry_point_start, entry_point_end)
    return False, None, None, None


def buy_signal_basic(ha_df, df):
    if len(ha_df) < 7:
        return False, None, None, None
    recent_ha = ha_df.iloc[-2:]
    past_ha = ha_df.iloc[-7:-2]
    recent_rsi = df['RSI'].iloc[-1] > 30
    ema9 = df['EMA9'].iloc[-1]
    ema26 = df['EMA26'].iloc[-1]
    ema_condition = ema9 > ema26
    if all(recent_ha['HA_Close'] > recent_ha['HA_Open']) and all(
            past_ha['HA_Close'] < past_ha[
                'HA_Open']) and recent_rsi and ema_condition:
        stop_loss = past_ha['HA_Low'].min()
        entry_price = df['Close'].iloc[-1]
        risk_amount = entry_price - stop_loss
        target_price = entry_price + (2 * risk_amount)
        # Define entry point range as from the EMA9 up to 1% above it
        entry_point_start = ema9
        entry_point_end = ema9 * 1.01
        return True, stop_loss, target_price, (
            entry_point_start, entry_point_end)
    return False, None, None, None
