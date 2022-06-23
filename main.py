from pymed import PubMed
import requests
import json
import xmltodict


# Create a PubMed object that GraphQL can use to query
# Note that the parameters are not required but kindly requested by PubMed Central
# https://www.ncbi.nlm.nih.gov/pmc/tools/developers/
pubmed = PubMed(tool="MyTool", email="my@email.address")

# Create a GraphQL query in plain text
query = "(Old adults + major depressive disorder + generalized anxiety disorder)"
# query="Effect of a Web-Based Cognitive Behavior Therapy for Insomnia Intervention With 1-"

# Execute the query against the API
results = pubmed.query(query, max_results=1)

# print(list(results))
# Loop over the retrieved articles
author_ls=[]
affliation_ls=[]
keywords_ls=[]
art_id_ls=[]
pub_ls=[]
title_ls=[]
abst_ls=[]
# summary_ls=[]

# Loop over the retrieved articles
for article in results:
    keyword=None
    # Extract and format information from the article
    article_id = article.pubmed_id.split('\n')[0] 
    title=article.title
    if article.keywords:
        if None in article.keywords:
            article.keywords.remove(None)
        keyword = '", "'.join(article.keywords)
    publication_date = article.publication_date
    abstract = article.abstract
    response=requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id='+str(article_id))
    strResponse=response.text #turn byte to json
    if abstract == '':
      abstract=strResponse.split('abstract')[1].split('",')[0]
    
    
    if abstract is None:
      # continue  # Filtered out articles without abstract
      sum_abst=""
    else:
      sum_abst=summarize(abstract) 
       
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

d={'Title':title_ls,'Article id':art_id_ls, 'Publication Date':pub_ls, \
   'Authors':author_ls, 'Affliations':affliation_ls, 'Abstract':abst_ls}
df=pd.DataFrame(d)