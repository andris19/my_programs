days=input('Days after 9/25/09: ')
days_int=int(days)
fjarlaegd_i_upphafi_i_milum=int(16637000000)
hradi_i_milum=int(38241)
fjarlaegd_a_dag_i_milum=int(hradi_i_milum*24)
distance_in_miles=int(fjarlaegd_i_upphafi_i_milum+fjarlaegd_a_dag_i_milum*days_int)
print('Miles from the sun: ',distance_in_miles)
miles_to_km=1.609344
distance_in_km=distance_in_miles*miles_to_km
print('Kilometers from the sun: ',round(distance_in_km))
AU_to_miles=92955887.6
distance_in_AU=distance_in_miles*(1/AU_to_miles)
print('AU from the sun: ',round(distance_in_AU))
