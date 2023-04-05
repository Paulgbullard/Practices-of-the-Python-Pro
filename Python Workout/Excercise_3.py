#Write a function that asks how long it took to run 10k
#Continue to ask how long it took for additional runs until the user presses enter
#Calculate and display the average time it took, before exiting

def run_timings():
    total_time = 0
    run_count = 0
    while True:
        entered_time = input("How long did it take (minutes)? : ")
        if not entered_time:
            print(f"Average time was {total_time/run_count}, over {run_count} runs")
            break
        else:
            total_time += float(entered_time)
            run_count += 1

run_timings()
