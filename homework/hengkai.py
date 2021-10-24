def bounce_result_height(h, n):
  if n == 1:
    return h
  else:
    return bounce_result_height((h/2), n-1)
def bounce_total_height(h, n):
  if n == 1:
    return 2 * (h/2 + h) - h
  else:
    return (2 * (bounce_total_height(h/2, n-1)))
print(bounce_result_height(100, 10))
print(bounce_total_height(100, 10))

