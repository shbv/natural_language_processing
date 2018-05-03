# Files needed:

### The following files have "--> To be Downloaded" if they are not provided with this zip file and need to be downloaded. For others, extra information is provided with "--> <Comment>"


input/

	train.csv				--> To be Downloaded

	test.csv				--> To be Downloaded

src/

	spooky_author_identification.ipynb	--> ipython notebook source code

scratch/

	gensim.20.txt				--> word vectors using gensim

	glove.6B.100d.txt			--> To be Downloaded
	
reports/

	spooky_author_identification.html	--> html version of ipynb source code

	Project_proposal_MLND.pdf		--> Project proposal pdf

	Project_report_MLND.pdf			--> Project report pdf
	
### For train.csv and test.csv, Download them from kaggle website to input/ subdirectory
Website: https://www.kaggle.com/c/spooky-author-identification/data

After downloading:

	cd input/

	unzip train.zip

	unzip test.zip

	cd ../

### For glove.6B.100d.txt: Download the following file into scratch/ subdirectory
Website: https://nlp.stanford.edu/data/glove.6B.zip

After downloading:

	cd scratch/

	unzip glove.6B.zip

	Check that glove.6B.100d.txt file exists in current directory (i.e. scratch/)

	cd ../

### Gensim does not need to be installed since word vectors are already generated and stored as scratch/gensim.20.txt. The ipynb comments disables the call to create gensim word vectors using "create_gensim_wordvectors" = 0
conda install -c anaconda gensim



# Packages needed:
### XGboost package is needed
conda install -c conda-forge xgboost



# Running notebook
cd src/

jupyter notebook spooky_author_identification.ipynb
