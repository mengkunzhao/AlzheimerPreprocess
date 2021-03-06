__author__ = 'Haohan Wang'

def getSubset():
    subsetIndex = [1, 2, 4, 5, 6]
    traits = [line.strip().split(',') for line in open('traits.csv')]
    traits_d = [line.strip() for line in open('traits_d.csv')]

    traits_new = []
    for line in traits:
        m = []
        for s in subsetIndex:
            try:
                tmp = float(line[s])
            except:
                tmp = 0
            m.append(str(tmp))
        traits_new.append(m)
    f1 = open('traits_sub.csv', 'w')
    for line in traits_new:
        f1.writelines(','.join(line)+'\n')
    f1.close()

    f2 = open('traits_d_sub.csv', 'w')
    for s in subsetIndex:
        f2.writelines(traits_d[s]+'\n')
    f2.close()

def getSubsetSNP():
    snps = [line.strip().split(',') for line in open('snps.csv')]
    markers = [line.strip() for line in open('marker.csv')]

    snps_new = []
    for line in snps:
        snps_new.append(line[:100])
    f1 = open('snps_sub.csv', 'w')
    for line in snps_new:
        f1.writelines(','.join(line)+'\n')
    f1.close()

    f2 = open('markers_sub.csv', 'w')
    for i in range(100):
        f2.writelines(markers[i]+'\n')
    f2.close()

if __name__ == '__main__':
    getSubsetSNP()