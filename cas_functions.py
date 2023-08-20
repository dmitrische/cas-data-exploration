def fatal_agg1(attributes, df_in):
	
	"""
	Function aggregating fatality counts over crashes featuring
	a particular attribute, with the attributes specified by the
	supplied list of attributes.
	
	INPUTS:
	------
	
	attributes - list of strings representing crash attributes
	
	df_in - CAS dataframe with rows spanning crashes and columns 
			spanning crash attributes
	
	OUTPUTS:
	-------
	
	df_out - reduced dataframe with the rows spanning crash 
			 attributes and 5 columns: 'crashes', 'fatalCrashes', 
			 'fatalities', 'fatal_fraction', and 'fatality_rate'. 
	
	"""
	
	import pandas as pd
	
	crashes = []
	fatal = []
	fatalities = []
	
	for a in attributes:
		# Count crashes involving at least one of given attribute
		crashes.append(len(df_in[(df_in[a] > 0)]))
		# Count how many of the above crashes are fatal (i.e. 1 or more fatalities)
		fatal.append(len(df_in[(df_in[a] > 0) & (df_in['fatalCount'] > 0)]))
		# Count all the fatalities for the above attribute-specific crashes
		fatalities.append(int(df_in[(df_in[a] > 0)]['fatalCount'].sum()))
	
	df_out = pd.DataFrame( 
		{
			'crashes':crashes,
			'fatalCrashes':fatal,
			'fatalities':fatalities
		},
		index = attributes
	)
	
	df_out['fatal_fraction'] = df_out['fatalCrashes']/df_out['crashes']
	df_out['fatality_rate'] = df_out['fatalities']/df_out['crashes']
	
	return df_out


def fatal_agg2(attributes1, attributes2, df_in):
	
	"""
	Function aggregating fatality counts over crashes featuring 
	a particular pair of attributes, with the pairs specified by 
	two supplied lists of attributes.
	
	INPUTS:
	------
	
	attributes1 - list of strings representing crash attributes
	attributes2 - list of strings representing crash attributes
	
	df_in - CAS dataframe with rows spanning crashes and columns 
			spanning crash attributes
	
	OUTPUTS:
	-------
	
	df_out - reduced dataframe with the rows spanning crash 
			 attributes and 5 columns: 'crashes', 'fatalCrashes', 
			 'fatalities', 'fatal_fraction', and 'fatality_rate'. 
	
	"""
	
	import pandas as pd
	import numpy as np
	
	lol_crash = [[] for i in range(len(attributes1))]
	lol_fatal = [[] for i in range(len(attributes1))]
	lol_fatalfrac = [[] for i in range(len(attributes1))]
	
	for i in range(len(attributes1)):
		vi = attributes1[i]
		for vj in attributes2:
			if(vi==vj):
				crash_count = len(df_in[(df_in[vi] > 1)])
				fatal_count = len(df_in[(df_in[vi] > 1) & (df_in['fatalCount'] > 0)])
			else:
				crash_count = len(df_in[(df_in[vi] > 0) & (df_in[vj] > 0)])
				fatal_count = len(df_in[(df_in[vi] > 0) & (df_in[vj] > 0) 
														& (df_in['fatalCount'] > 0)])
			
			lol_crash[i].append(crash_count)
			lol_fatal[i].append(fatal_count)
			if(crash_count > 0):
				lol_fatalfrac[i].append(fatal_count/crash_count)
			else:
				lol_fatalfrac[i].append(np.nan)

	crashmat_df = pd.DataFrame(lol_crash,columns=attributes2, index=attributes1)
	fatalmat_df = pd.DataFrame(lol_fatal,columns=attributes2, index=attributes1)
	fatalfracmat_df = pd.DataFrame(lol_fatalfrac,columns=attributes2, index=attributes1)
	
	output = {'crashmat_df':crashmat_df, 
				'fatalmat_df':fatalmat_df, 
				'fatalfracmat_df':fatalfracmat_df}
	
	return output

# https://stackoverflow.com/questions/46715736/rotating-the-column-name-for-a-pandas-dataframe
def format_vertical_headers(df):
    """Display a dataframe with vertical column headers"""
    styles = [dict(selector="th", props=[('width', '40px')]),
              dict(selector="th.col_heading",
                   props=[("writing-mode", "vertical-rl"),
                          ('transform', 'rotateZ(180deg)'), 
                          ('height', '150px'),
                          ('vertical-align', 'top')])]
    return (df.fillna('').style.set_table_styles(styles))


