# per list sa tangkal represents the lugwa,
# so, naa tay tangkal nga naay 4 ka lugwa,
# and per lugwa, naay sud nga mga manok
tangkal = [
    ["bisaya", "45 days"],
    ["45 days", "45 days"],
    ["bisaya", "bisaya", "bisaya", "bisaya"],
    ["bisaya", "bisaya", "bisaya", ]
]
# i print ang manok nga bisaya sa kinaunahan nga lugwa
print(tangkal[0][0])

# ilisan ug manok bisaya ang 45 days sa kinaunahan nga lugwa
tangkal[0][1] = "bisaya"

# ihawun ang manok nga bisaya sa kinaunahan nga lugwa
# in other words, i remove and manok sa tankal (list)
tangkal[0].remove("bisaya")

