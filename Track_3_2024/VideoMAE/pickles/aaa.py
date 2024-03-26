import pickle
import os

def load_k_fold_probs(pickle_dir, view, k=5):
    probs = []
    for i in range(k):
        with open(os.path.join(pickle_dir, "A2_{}_vmae_16x4_crop_fold{}.pkl".format(view, i)), "rb") as fp:
            vmae_16x4_probs = pickle.load(fp)
        probs.append(vmae_16x4_probs)
    return probs

k_flod_dash_probs = load_k_fold_probs('A2', "dash")
k_flod_right_probs = load_k_fold_probs('A2', "right")
k_flod_rear_probs = load_k_fold_probs('A2', "rear")
print(sorted(k_flod_rear_probs[0].keys()))
