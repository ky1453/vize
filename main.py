import pandas as pd

age_array = [15, 15, 16, 19, 19, 20, 20, 21, 22, 28, 35, 40, 41, 42, 43, 44, 60, 61, 65]
c1 = 16
c2 = 22

last_c1 = c1
last_c2 = c2

for i in range(1, 5):
    c1_sum = 0
    c2_sum = 0
    c1_elements = 0
    c2_elements = 0

    for age in age_array:
        c1_distance = abs(age - last_c1)
        c2_distance = abs(age - last_c2)
        if c2_distance > c1_distance:
            nearest_cluster = last_c1
        elif c1_distance >= c2_distance:
            nearest_cluster = last_c2

        if nearest_cluster == last_c2:
            c2_elements += 1
            c2_sum += age
        elif nearest_cluster == last_c1:
            c1_elements += 1
            c1_sum += age

    c1 = c1_sum / c1_elements
    c2 = c2_sum / c2_elements

    cluster_labels = ['1' if abs(age - last_c1) < abs(age - last_c2) else '2' for age in age_array]
    new_clusters = [c1 if label == '1' else c2 for label in cluster_labels]

    data = {
        'Xi': age_array,
        'C1': [last_c1] * len(age_array),
        'C2': [last_c2] * len(age_array),
        'Distance 1': [abs(age - last_c1) for age in age_array],
        'Distance 2': [abs(age - last_c2) for age in age_array],
        'Nearest Cluster': cluster_labels,
        'New Centroid': new_clusters
    }

    df = pd.DataFrame(data)

    print(f"Iteration {i}:")
    print(df)

    last_c1 = c1
    last_c2 = c2
