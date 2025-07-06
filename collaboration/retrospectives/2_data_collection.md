# 🌀 Retrospective: Milestone 2 - Data Collection

> “Regardless of what we discover, we understand and truly believe that everyone
> did the best job they could, given what they knew at the time, their skills
> and abilities, the resources available, and the situation at hand.”
>
> - [Norm Kerth](http://www.amazon.com/Project-Retrospectives-Handbook-Reviews-Dorset-ebook/dp/B00DY3KQJU/ref=tmm_kin_swatch_0?_encoding=UTF8&sr=&qid=)

All done :)

This retrospective is meant for looking back at how Milestone 2: Data
Collection went and learning what to do differently next time.

## Behaviors, not People

Focus on what your group can _do_ that will make the next sprint better. Keep
your retrospectives _positive_ and _general_. __You should NEVER mention people
by name!!!__

- __What parts of your plan went as expected?__
  - The structured approach to data selection and justification worked very
    well, allowing us to systematically evaluate candidate datasets against
    our research question and project constraints.
  - The division of tasks for initial data exploration and documentation was
    effective.
  - The collaboration on identifying and acquiring the primary dataset (SED)
    was smooth.

- __What parts of your plan did not work out?__
  - Underestimating the computational resources required for processing very
    large raw data files (like `SED_Student_log.csv`) within the sandbox
    environment led to delays in automated data dictionary generation and
    initial cleaning execution.
  - Initial assumptions about direct download link reliability for all
    external datasets proved incorrect (e.g., Kaggle 403 error).

- __Did you need to add things that weren't in your strategy?__
- __Stop Doing__
  - __Assuming sandbox capabilities for very large datasets:__ For future
    milestones involving large data, we should proactively assess
    computational requirements and plan for local execution or alternative
    cloud resources from the outset.
  - __Relying solely on single-source download links:__ For critical external
    data, we should always have backup acquisition strategies or verify link
    persistence early.

- __Continue Doing__
  - __Structured evaluation:__ The systematic approach to evaluating datasets
    (using criteria like relevance, quality, granularity, and practical
    considerations) was highly effective and should be continued for any
    future data acquisition.
  - __Detailed documentation:__ Creating dedicated reports (like
    `data_processing_report.md`) and comprehensive `README.md` files for each
    phase significantly improves clarity and reproducibility.
  - __Collaborative problem-solving:__ When encountering technical blockers
    (e.g., sandbox limitations), leveraging team members' local environments
    for processing was an effective workaround.

- __Start Doing__
  - __Early resource assessment:__ Before starting data processing,
    explicitly assess the computational resources needed for the expected
    data volume and complexity.
  - __Version control for cleaned data:__ Implement a clear strategy for
    versioning and storing cleaned datasets, especially if they are
    generated through complex pipelines.
  - __Automated data quality checks:__ Integrate basic automated data
    quality checks into our cleaning scripts to catch common issues early.

- __Lessons Learned__
  - __Data is messy, and that's okay:__ Even with well-defined problems,
    real-world data presents unexpected challenges (size, format,
    missingness), and adaptability is key.
  - __The importance of the data pipeline:__ Understanding the flow from raw
- We successfully __identified and selected a suitable dataset__ that aligned
  with our project focus on student engagement.
- Our __scripted exploration tools__ worked well to inspect the structure and
  health of each dataset.
- Creating __data dictionaries__ allowed us to document features.
- We __underestimated the complexity of the raw data__, especially merging
  inconsistently structured CSVs.
- Some __file paths and documentation standards__ needed adjustment after
  initial confusion due to directory changes.
- We created a __dedicated exploratory script (`explore_sed_data.py`)__ to
  inspect and summarize datasets before cleaning.
- We included a __data processing report__ to communicate preprocessing
  decisions more clearly.
- We simplified the initial cleaning process by focusing on essential columns
  and omitting overly detailed transformations that could wait until analysis.
- Creating __data dictionaries__ allowed us to document features systematically
  and ensure transparency.

- __What parts of our plan did not work out?__
  - We __underestimated the complexity of the raw data__, especially merging
    inconsistently structured CSVs.
  - Some __file paths and documentation standards__ needed adjustment after
    initial confusion due to directory changes.

- __Assuming dataset readiness__: We sometimes assumed data would be
  immediately usable. We should always allocate time for deep inspection.
- __Manual patching__: Avoid ad hoc fixes; instead, build reproducible scripts
  from the start.
- __Late naming conventions__: Inconsistent filenames and paths caused small
  setbacks—naming should be standardized earlier.
- __Exploratory scripting__: Generating `.info()` and `.head()` views for each
  CSV helped us quickly grasp structure and potential issues.
- __Data dictionary generation__: Automatically documenting datasets using
  markdown tables was helpful for both transparency and collaboration.
- __Collaborative debugging__: Quick syncs when data issues arose allowed us to
  align and move forward efficiently.
- __Pre-flight file structure check__: Verify and agree on directory structures
  and script paths before coding begins.
- __Data health checklist__: Build a checklist for data readiness that includes
  null value inspection, consistent key formats, and expected joins.
- __Leverage version control for raw files__: Even with large files, it’s
  useful to track metadata or hashes to know when datasets change.
- __Documentation is part of the data__: Clear data dictionaries and structured
  outputs are not just helpful—they are essential for downstream tasks.
- __Preparation scripts are reusable assets__: Our `explore_sed_data.py` is a
  strong tool that can support future iterations or similar projects.
- __Data issues can cascade__: Small data quality issues left unaddressed early
  can lead to confusion and delays later.
- __A clean dataset enables creativity__: By resolving inconsistencies and
  documenting features, we set ourselves up for efficient exploration and
  hypothesis generation in Milestone 3.

- __Assuming dataset readiness__: We sometimes assumed data would be immediately
  usable. We should always allocate time for deep inspection.
- __Manual patching__: Avoid ad hoc fixes; instead, build reproducible scripts  
  from the start.
- __Late naming conventions__: Inconsistent filenames and paths caused small  
  setbacks—naming should be standardized earlier.
- __Exploratory scripting__: Generating `.info()` and `.head()` views for each  
  CSV helped us quickly grasp structure and potential issues.
- __Data dictionary generation__: Automatically documenting datasets using  
  markdown tables was helpful for both transparency and collaboration.
- __Collaborative debugging__: Quick syncs when data issues arose allowed us to
  align and move forward efficiently.
- __Pre-flight file structure check__: Verify and agree on directory structures
  and script paths before coding begins.
- __Data health checklist__: Build a checklist for data readiness that includes
  null value inspection, consistent key formats, and expected joins.
- __Leverage version control for raw files__: Even with large files, it’s  
  useful to track metadata or hashes to know when datasets change.
- __Documentation is part of the data__: Clear data dictionaries and structured
  outputs are not just helpful—they are essential for downstream tasks.
- __Preparation scripts are reusable assets__: Our `explore_sed_data.py` is a  
  strong tool that can support future iterations or similar projects.
- __Data issues can cascade__: Small data quality issues left unaddressed early
  can lead to confusion and delays later.
- __A clean dataset enables creativity__: By resolving inconsistencies and  
As we move into the next phase of data exploration, we carry forward both  
working tools and hard-won insight. This milestone clarified the value of  
thorough data review and repeatable preprocessing. We are now better prepared  
to generate insights with confidence.
  hypothesis generation in Milestone 3.
- __Assuming dataset readiness__: We sometimes assumed data would be immediately
  usable. We should always allocate time for deep inspection.
- __Manual patching__: Avoid ad hoc fixes; instead, build reproducible scripts
  from the start.
- __Late naming conventions__: Inconsistent filenames and paths caused small
  setbacks—naming should be standardized earlier.

## ✅ Continue Doing

- __Exploratory scripting__: Generating `.info()` and `.head()` views for each
  CSV helped us quickly grasp structure and potential issues.
- __Data dictionary generation__: Automatically documenting datasets using markdown
    tables was helpful for both transparency and collaboration.
- __Collaborative debugging__: Quick syncs when data issues arose allowed us to
  align and move forward efficiently.

### 🆕 Start Doing

- __Pre-flight file structure check__: Verify and agree on directory structures
  and script paths before coding begins.
- __Data health checklist__: Build a checklist for data readiness that includes
  null value inspection, consistent key formats, and expected joins.
- __Leverage version control for raw files__: Even with large files, it’s useful
  to track metadata or hashes to know when datasets change.

### 📚 Lessons Learned

- __Documentation is part of the data__: Clear data dictionaries and structured
  outputs are not just helpful—they are essential for downstream tasks.
- __Preparation scripts are reusable assets__: Our `explore_sed_data.py` is a
  strong tool that can support future iterations or similar projects.
- __Data issues can cascade__: Small data quality issues left unaddressed
  early can lead to confusion and delays later.
- __A clean dataset enables creativity__: By resolving inconsistencies and
  documenting features, we set ourselves up for efficient exploration and
  hypothesis generation in Milestone 3.

---

As we move into the next phase of data exploration, we carry forward both working
  tools and hard-won insight. This milestone clarified the value of thorough
    data review and repeatable preprocessing. We are now better prepared to
    generate insights with confidence.

## Individual Retrospectives

### Caesar

having many datasets to choose from just makes everything more difficult.
