def observed():
    observations = []
    for i in range(5):
        user_observation = input("Please enter an observation:")
        observations.append(user_observation)
    return observations


def remove_observations(a=[]):
    while True:
        user_answer = input("Do you wish to remove an observation (yes/no)?").lower()
        if user_answer == "yes":
            user_response = input("What observation do you wish to remove?")
            if user_response in a:
                a.remove(user_response)
                print("Done!")
        else:
            break


def run():
    observations_list = observed()
    remove_observations(observations_list)
    results = {}

    print("Observations:")
    for i in observations_list:
        if i not in results:
            results[i] = observations_list.count(i)

    for x in results.keys():
        print(f"{x} observed {results[x]} times")


run()