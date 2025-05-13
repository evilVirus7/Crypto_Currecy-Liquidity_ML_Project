# 📊 Exploratory Data Analysis Report

## 📁 Dataset Overview
- **Total records**: 1000 (from 2 dates: 2022-03-16 & 2022-03-17)
- **Unique cryptocurrencies**: 506
- **Key columns**:
  - `price`: Current coin price
  - `1h`, `24h`, `7d`: Price changes in time windows
  - `24h_volume`: 24-hour trading volume
  - `mkt_cap`: Market capitalization

## 🧼 Data Cleaning
- Missing values found in `1h`, `24h`, `7d`, `24h_volume` (7–8 entries)
- Handled using median imputation

## 🔍 Feature Engineering
- `liquidity_score = (24h_volume / mkt_cap) * abs(7d_change)`
- `log_volume`, `log_mkt_cap`: Log-transformed for normalization
- `ma_7`: 2-day moving average of price per coin symbol

## 📈 Key Distributions
- **Liquidity Score**: Skewed right — most coins have low liquidity
- **Volume & Market Cap**: Power law distribution — few coins dominate

## 🔗 Correlations
| Feature A        | Feature B        | Correlation |
|------------------|------------------|-------------|
| 24h_volume       | mkt_cap          | 0.89        |
| liquidity_score  | 24h_volume       | 0.63        |
| liquidity_score  | 7d               | 0.47        |

## 🪙 Top 10 Coins by Average Liquidity
1. Bitcoin (BTC)
2. Ethereum (ETH)
3. Tether (USDT)
4. Binance Coin (BNB)
5. USD Coin (USDC)
6. Solana (SOL)
7. Avalanche (AVAX)
8. Terra (LUNA)
9. XRP (XRP)
10. Cardano (ADA)

## 📌 Key Insights
- Liquidity is highly influenced by volume and market cap.
- Volatility amplifies liquidity, especially in smaller-cap coins.
- A few major cryptocurrencies stabilize the market.

## 📎 Recommendations for Modeling
- Normalize skewed variables (log scale)
- Include moving averages and volatility in feature set
- Target variable: `liquidity_score`
