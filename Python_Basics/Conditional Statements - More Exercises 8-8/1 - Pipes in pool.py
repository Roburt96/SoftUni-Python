V = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())

pipe1 = P1 * H
pipe2 = P2 * H
total = pipe1 + pipe2
total_percent = (total * 100) / V
remaining = total - V
pipe1_percent = (pipe1 * 100) / total
pipe2_percent = (pipe2 * 100) / total

if total <= V:
    print(f"The pool is{total_percent: .2f}%  full. Pipe 1:{pipe1_percent: .2f}%. Pipe 2:{pipe2_percent: .2f}%.")
else:
    print(f"For{H: .2f} hours the pool overflows with{remaining: .2f} liters.")
