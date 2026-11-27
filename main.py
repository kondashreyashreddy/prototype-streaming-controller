from var import u1, service_input, show_input, episode_input, site, Crunchyroll, Netflix, YouTube, Amazon
from source import lin, sys_check1, sys_check2, sys_check3

print(lin())
for s in site:
    u1 += 1
    print(f"{u1}. {s}")
service_input = input("\nEnter Name Of Streaming Service Of Choice: ")
chose = sys_check1(service_input)

print(lin())
u1 = 0
for c in chose:
    u1 += 1
    print(f"{u1}. {c}")
show_input = input("\nEnter Name Of Show: ")
chose1 = sys_check2(show_input, chose)

episode_input = input("Enter Season/Movie Of Choice: ")
chose2 = sys_check3(episode_input, chose1)
