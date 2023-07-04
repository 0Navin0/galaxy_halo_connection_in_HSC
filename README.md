# galaxy_halo_connection_in_HSC
This repository contains various measurements performed for the publication titled - "Galaxy-dark matter connection of photometric galaxies from the HSC-SSP Survey: Galaxy-galaxy lensing and the halo model"

Files and Directories:

	`radialbins.csv`: The 10 radial bins used for the measurement of lensing signals in this work.

	`abundances`: measurements of abundaces of the stellar mass threshold lens samples.

	`WLS_lenses_threshold_bins`: Measured Weak Lensing Signals for the same thresholds.
		`wls_zbin_*.csv`: the signals for redshift bins 1 and 2.

	`WLS_covariance_matrices`: Covariance matrices obtained from above measurements using Jackknife technique.
		`cov_mat_z*_stelM_thresh_*.txt`: Covariance matrices for the 10 radial bins.
		`stddev_hsc`: standad deviation error of the lensing signal in each of the 10 radial bins, obtained for each stellar mass threshold sample - square root of the diagonal components of the matrices.
	
