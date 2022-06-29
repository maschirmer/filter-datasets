##TODO

Blogs and News:

- run create_blogs_data.py again;

- split by ".?!", removed sentences below 4 characters, 
- shape: (4644644, 1)
- should be all english language (without proof)
- quantity of blogs : newsarticles not known, maybe not 50:50

Reddit:

- just used ~50% of original data:
    - 20 million entrys to split up
- finish build:
    - splitting up strings, removing short ones / anomaly strings


Twitter:

- look for flaws, build again


- balance the three datasets in terms of proprtion randomly


write script for other filter:

- get a dataset per mode (twitter, reddit, blogsnews)
- with one column calssification from my method (static_filter)
- another column with classification from the other method (ftr_classifier)