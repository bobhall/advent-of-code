

fd = open('bob.tmp', 'r')
years = fd.readlines()


years = [int(year.strip()) for year in years]



for ix in range(0,len(years)):
    for jx in range(ix+1, len(years)):
        for nx in range(jx+1, len(years)):
            if years[ix] + years[jx] + years[nx] == 2020:
                print("Found it!! {}".format((years[ix], years[jx], years[nx])))
