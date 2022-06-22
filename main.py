from pymed import PubMed


# Create a PubMed object that GraphQL can use to query
# Note that the parameters are not required but kindly requested by PubMed Central
# https://www.ncbi.nlm.nih.gov/pmc/tools/developers/
pubmed = PubMed(tool="MyTool", email="my@email.address")

# Create a GraphQL query in plain text
query = "(Old adults + acute LBP + Low Back Pain)"


# Execute the query against the API
results = pubmed.query(query, max_results=10)

# print(list(results))
# Loop over the retrieved articles
author_ls=[]
affliation_ls=[]
keywords_ls=[]
art_id_ls=[]
pub_ls=[]
title_ls=[]
abst_ls=[]

# Loop over the retrieved articles
for article in results:
    keyword=None
    # Extract and format information from the article
    article_id = article.pubmed_id.split('\n')[0] 
    title = article.title
    if article.keywords:
        if None in article.keywords:
            article.keywords.remove(None)
        keyword = '", "'.join(article.keywords)
    publication_date = article.publication_date
    abstract = article.abstract

    if keyword is None:
        keyword=""
    
    cur_author_ls=[]
    cur_aff_ls=[]     
    for d in article.authors:
        name=d.get('firstname')+' '+ d.get('lastname')
        aff=d.get('affiliation')
        if aff is None:
          aff='UNKNOWN'
        cur_author_ls.append(name)
        cur_aff_ls.append(aff)
    author_ls.append(cur_author_ls)
    affliation_ls.append(cur_aff_ls)
    


    keywords_ls.append(keyword)
    art_id_ls.append(article_id)
    pub_ls.append(publication_date)
    title_ls.append(title)
    abst_ls.append(abstract)
print(art_id_ls)
