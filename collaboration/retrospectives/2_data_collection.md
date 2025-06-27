# 🌀 Retrospective: Milestone 2 - Data Collection

> *"Regardless of what we discover, we understand and truly believe that  
> everyone did the best job they could, given what they knew at the time,  
> their skills and abilities, the resources available, and the situation  
> at hand."*  
> — Norm Kerth

This retrospective reflects on our progress through **Milestone 2: Data  
Collection**. We focused on acquiring, validating, and preparing our dataset  
to ensure a strong foundation for the next analytical steps. This stage was  
crucial for aligning our data with the research question and setting up clean,  
well-documented inputs.

* We successfully **identified and selected a suitable dataset** that aligned
    with our project focus on student engagement.
  * Our **scripted exploration tools** worked well to inspect the structure and
    health of each dataset.
  * Creating **data dictionaries** allowed us to document features  
  * We **underestimated the complexity of the raw data**, especially merging  
    inconsistently structured CSVs.
  * Some **file paths and documentation standards** needed adjustment after  
    initial confusion due to directory changes.
  * We created a **dedicated exploratory script (`explore_sed_data.py`)** to  
    inspect and summarize datasets before cleaning.
  * We included a **data processing report** to communicate preprocessing  
    decisions more clearly.
  * We simplified the initial cleaning process by focusing on essential columns
    and omitting overly detailed transformations that could wait until analysis.
  * Creating **data dictionaries** allowed us to document features systematically
    and ensure transparency.

* **What parts of our plan did not work out?**
  * We **underestimated the complexity of the raw data**, especially merging
    inconsistently structured CSVs.
  * Some **file paths and documentation standards** needed adjustment after initial
    confusion due to directory changes.

* **Assuming dataset readiness**: We sometimes assumed data would be immediately
  usable. We should always allocate time for deep inspection.
* **Manual patching**: Avoid ad hoc fixes; instead, build reproducible scripts  
  from the start.
* **Late naming conventions**: Inconsistent filenames and paths caused small  
  setbacks—naming should be standardized earlier.
* **Exploratory scripting**: Generating `.info()` and `.head()` views for each  
  CSV helped us quickly grasp structure and potential issues.
* **Data dictionary generation**: Automatically documenting datasets using  
  markdown tables was helpful for both transparency and collaboration.
* **Collaborative debugging**: Quick syncs when data issues arose allowed us to
  align and move forward efficiently.
* **Pre-flight file structure check**: Verify and agree on directory structures
  and script paths before coding begins.
* **Data health checklist**: Build a checklist for data readiness that includes
  null value inspection, consistent key formats, and expected joins.
* **Leverage version control for raw files**: Even with large files, it’s  
  useful to track metadata or hashes to know when datasets change.
* **Documentation is part of the data**: Clear data dictionaries and structured
  outputs are not just helpful—they are essential for downstream tasks.
* **Preparation scripts are reusable assets**: Our `explore_sed_data.py` is a  
  strong tool that can support future iterations or similar projects.
* **Data issues can cascade**: Small data quality issues left unaddressed early
  can lead to confusion and delays later.
* **A clean dataset enables creativity**: By resolving inconsistencies and  
As we move into the next phase of data exploration, we carry forward both  
working tools and hard-won insight. This milestone clarified the value of  
thorough data review and repeatable preprocessing. We are now better prepared  
to generate insights with confidence.
  hypothesis generation in Milestone 3.
* **Assuming dataset readiness**: We sometimes assumed data would be immediately
  usable. We should always allocate time for deep inspection.
* **Manual patching**: Avoid ad hoc fixes; instead, build reproducible scripts
  from the start.
* **Late naming conventions**: Inconsistent filenames and paths caused small
  setbacks—naming should be standardized earlier.

## ✅ Continue Doing

* **Exploratory scripting**: Generating `.info()` and `.head()` views for each
  CSV helped us quickly grasp structure and potential issues.
* **Data dictionary generation**: Automatically documenting datasets using markdown
    tables was helpful for both transparency and collaboration.
* **Collaborative debugging**: Quick syncs when data issues arose allowed us to
  align and move forward efficiently.

### 🆕 Start Doing

* **Pre-flight file structure check**: Verify and agree on directory structures
  and script paths before coding begins.
* **Data health checklist**: Build a checklist for data readiness that includes
  null value inspection, consistent key formats, and expected joins.
* **Leverage version control for raw files**: Even with large files, it’s useful
  to track metadata or hashes to know when datasets change.

### 📚 Lessons Learned

* **Documentation is part of the data**: Clear data dictionaries and structured
  outputs are not just helpful—they are essential for downstream tasks.
* **Preparation scripts are reusable assets**: Our `explore_sed_data.py` is a
  strong tool that can support future iterations or similar projects.
* **Data issues can cascade**: Small data quality issues left unaddressed
  early can lead to confusion and delays later.
* **A clean dataset enables creativity**: By resolving inconsistencies and
  documenting features, we set ourselves up for efficient exploration and
  hypothesis generation in Milestone 3.

---

As we move into the next phase of data exploration, we carry forward both working
  tools and hard-won insight. This milestone clarified the value of thorough
    data review and repeatable preprocessing. We are now better prepared to
    generate insights with confidence.
