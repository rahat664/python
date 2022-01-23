saarc = ["Bangladesh", "India", "Nepal", "Bhutan", "Pakistan", "Srilanka", "Afghanistan"]
print(saarc)
print(saarc[0])
print("number of countries in SAARC:", len(saarc))
print("Bangladesh" in saarc)
print("China" in saarc)
country = input("Enter the name of the country:")
if country in saarc:
    print(country, "is a member of SAARC")
else:
    print(country, "is not a member of SAARC")
