import ncepbufr,sys
# print satids and counts for obsuv8 bufr dumps.
satid_dict={200:'NOAA-8',201:'NOAA-9',202:'NOAA-10',203:'NOAA-11',204:'NOAA-12',205:'NOAA-14',206:'NOAA-15',207:'NOAA-16',207:'NOAA-18',209:'NOAA-19'}
bufr = ncepbufr.open(sys.argv[1])
satids = []
while bufr.advance() == 0: # loop over messages.
    while bufr.load_subset() == 0: # loop over subsets in message.
       hdr = bufr.read_subset("SAID") #parse header string
       satids.append(int(hdr[0][0]))
satids_uniq = list(set(satids))
ozinv = ['%s: %s, ' % (satid_dict[sat], satids.count(sat)) for sat in satids_uniq]
print("".join(ozinv)[:-2])
bufr.close()
