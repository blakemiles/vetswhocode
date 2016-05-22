# DAO Contract Calculator
# inputs current rates for BTC/ETH/DAO
# returns USD in DAO contract and rate since start
btcUSD = raw_input("Enter current BTC/USD rate: ")
btcETH = raw_input("Enter current BTC/ETH rate: ")
daoContract = raw_input("Enter current amount of ETH in DAO contract: ")

btcDAO = float(btcETH) * float(daoContract)
usdDAO = float(btcDAO) * float(btcUSD)

print ""
print "Based on current rates..."
print "----------------"
print "BTC : {:,.4f}" .format(btcDAO)
print "USD : {:,.0f}" .format(usdDAO)
