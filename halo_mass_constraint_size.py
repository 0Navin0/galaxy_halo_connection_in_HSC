import pandas as pd

if __name__=="__main__":

    hmass_constraint = lambda m50,diff16,diff84: (10**(m50+diff84) - 10**(m50+diff16))/10**m50

    df = pd.read_csv("zbin_1_constraints.csv")
    print("redshift bin 1:")
    for cbin, diff in zip(df.stelM_thresh, hmass_constraint(df.avmass_50.values, df.avmass_16.values, df.avmass_84.values)*100):
        print(cbin, diff)

    df = pd.read_csv("zbin_2_constraints.csv")
    print("redshift bin 2:")
    for cbin, diff in zip(df.stelM_thresh, hmass_constraint(df.avmass_50.values, df.avmass_16.values, df.avmass_84.values)*100):
        print(cbin, diff)
