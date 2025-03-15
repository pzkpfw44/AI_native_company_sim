import random
import pandas as pd
from datetime import datetime

class AINativeCompany:
    def __init__(self, name="AI Corp"):
        self.name = name
        self.balance = 1000000  # Starting budget in any currency you want
        self.employees = 50  # Initial human workforce
        self.ai_agents = 10  # Initial AI workforce
        self.market_trend = 1.0  # Market health (1.0 = stable, <1 = downturn, >1 = growth)
        self.history = []

    def simulate_market(self):
        """Simulate a market fluctuation that impacts company revenue"""
        self.market_trend = round(random.uniform(0.8, 1.2), 2)
        return self.market_trend

    def ai_decision(self):
        """AI decides resource allocation: HR, R&D, Marketing, or Cost-cutting"""
        choices = ["HR Investment", "R&D", "Marketing", "Cost-cutting"]
        decision = random.choice(choices)
        impact = random.uniform(-50000, 100000)  # Financial impact of decision
        self.balance += impact
        return decision, impact

    def run_simulation_step(self):
        """Run a single step of company operations"""
        market = self.simulate_market()
        decision, impact = self.ai_decision()
        self.history.append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "market_trend": market,
            "decision": decision,
            "impact": impact,
            "balance": self.balance
        })
        return market, decision, impact, self.balance

    def get_company_status(self):
        """Return current company stats"""
        return {
            "Company Name": self.name,
            "Balance ($)": self.balance,
            "Employees": self.employees,
            "AI Agents": self.ai_agents,
            "Market Trend": self.market_trend
        }

if __name__ == "__main__":
    # Create instance
    company = AINativeCompany()

    # Run simulation for 10 steps
    for _ in range(10):
        market, decision, impact, balance = company.run_simulation_step()
        print(f"Market: {market} | AI Decision: {decision} | Impact: ${impact:.2f} | Balance: ${balance:.2f}")

    # Convert history to a DataFrame and display
    df = pd.DataFrame(company.history)
    print("\nSimulation Results:")
    print(df)

# END
