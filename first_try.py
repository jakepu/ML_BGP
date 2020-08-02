import dask as ds
df = ds.read_csv('update_m.txt', sep='|', usecols=[1,2,3,4,5], parse_dates=[1],infer_datetime_format = True)