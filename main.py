from madlibs import MadLibs


def main():
    md = MadLibs()
    bw = md.bag_of_words()
    bm = md.building_madlibs(bw=bw)
    md.madlibs_output(text=bm)


if __name__=='__main__':
    main()