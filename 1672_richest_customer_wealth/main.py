

def maximum_wealth(accounts):

  current_max = 0


  for account in accounts:
      current_account = 0

      for num in account:
        current_account += num
      current_max = max(current_max, current_account)

  return current_max

# output 6
# accounts = [[1,2,3],[3,2,1]]
# output 10
# accounts = [[1,5],[7,3],[3,5]]
# output 17
accounts = [[2,8,-7],[7,1,3],[1,9,-5]]

result = maximum_wealth(accounts)

print(result)
