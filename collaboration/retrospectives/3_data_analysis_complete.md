# Retrospective: Milestone 3 - Data Exploration and Analysis

> “Regardless of what we discover, we understand and truly believe that everyone
> did the best job they could, given what they knew at the time, their skills
> and abilities, the resources available, and the situation at hand.”
>
> - [Norm Kerth](http://www.amazon.com/Project-Retrospectives-Handbook-Reviews-Dorset-ebook/dp/B00DY3KQJU/ref=tmm_kin_swatch_0?_encoding=UTF8&sr=&qid=)

All done :)

This retrospective is meant for looking back at how Milestone 3: Data Exploration
and Analysis went and learning what to do differently next time.

## Behaviors, not People

Focus on what your group can _do_ that will make the next sprint better. Keep your
retrospectives _positive_ and _general_. **_You should NEVER mention people by name!!!_**

## Strategy vs. Board

- The structured approach to EDA (univariate, bivariate, multivariate analysis)
  helped us systematically explore the cleaned data and identify initial patterns.
- The use of Jupyter notebooks facilitated iterative analysis and visualization,
  making it easy to share progress and findings within the team.
- The focus on hypothesis testing helped us move from mere observation to
  statistically supported insights, aligning with the workshop's emphasis on
  confidence over correctness.
  - Integrating the concepts from the "Learning from Data" workshop, particularly
  - Initial attempts at complex modeling approaches were overly ambitious given the
    time constraints and the need for deeper feature engineering.
  - Visualizing certain multi-dimensional relationships proved challenging without
    more advanced visualization libraries or techniques.
  - Ensuring all team members were proficient with the same set of visualization
  - We found it necessary to spend more time on feature engineering than initially
    anticipated, as some raw features needed significant transformation to be useful
    for modeling.
  - We incorporated more interactive visualizations (e.g., using Plotly) to better
  - We decided to defer some highly complex model architectures to a later stage,
    focusing instead on simpler, interpretable models for preliminary insights, to
    ensure we met the milestone objectives within the timeframe.
    beneficial.

  - **Over-optimizing initial models:** For preliminary modeling, focus on
    interpretability and basic performance rather than immediately striving for
    state-of-the-art accuracy, which can be a time sink.
  - **Underestimating the time for data visualization:** Creating clear and
  - **Iterative EDA:** The cyclical process of exploring, visualizing, and analyzing
    data proved highly effective for uncovering patterns and validating hypotheses.
  - **Collaborative notebook development:** Working together on Jupyter notebooks,
    with clear sections and comments, facilitated knowledge sharing and code review.
  - **Focus on the research question:** Constantly linking our analysis back to the
  - **Early integration of domain expertise:** More frequent consultation with domain
    experts (if available) during EDA could have accelerated the identification of
    meaningful features and relationships.
  - **Standardize visualization libraries/tools:** Agreeing on a common set of
    visualization tools at the outset could streamline the process and ensure
  - **Analysis is an art and a science:** While algorithms provide the science, the
    art lies in asking the right questions, interpreting results critically, and
    effectively communicating insights.
  - **The power of visualization:** Effective data visualization is not just about
    pretty graphs; it's a powerful tool for discovery, communication, and
    identifying data quality issues.
_Fill out this template as a group, either in a call or asynchronously,
and place it in your repository as `collaboration/retrospectives/3_data_analysis.md`._
    models can often provide more immediate value than complex black-box models,
    especially when trying to understand underlying relationships.
    of the insights and their implications.

- **Did you need to add things that weren't in your strategy?**
  - We found it necessary to spend more time on feature engineering than initially
  anticipated, as some raw features needed significant transformation to be
  useful for modeling.
  - We incorporated more interactive visualizations (e.g., using Plotly)
  to better explore complex relationships,
  which wasn't explicitly planned but proved beneficial.

- **Or remove extra steps?**
  - We decided to defer some highly complex model architectures to a later stage,
  focusing instead on simpler, interpretable models for preliminary insights,
  to ensure we met the milestone objectives within the timeframe.

### The Four Points

- **Stop Doing**:
  - **Over-optimizing initial models:** For preliminary modeling, focus on
  interpretability and basic performance rather than immediately striving for
  state-of-the-art accuracy, which can be a time sink.
  - **Underestimating the time for data visualization:** Creating clear and
  insightful visualizations often takes more time than anticipated,
  especially when dealing with complex datasets.

- **Continue Doing**:
  - **Iterative EDA:** The cyclical process of exploring, visualizing,
  and analyzing data proved highly effective for uncovering patterns
  and validating hypotheses.
  - **Collaborative notebook development:** Working together on Jupyter notebooks,
  with clear sections and comments, facilitated knowledge sharing and code review.
  - **Focus on the research question:** Constantly linking our analysis back to
  the actionable research question ensured our efforts remained relevant and goal-oriented.

- **Start Doing**:
  - **Early integration of domain expertise:** More frequent consultation with
  domain experts (if available) during EDA could have accelerated the
  identification of meaningful features and relationships.
  - **Standardize visualization libraries/tools:** Agreeing on a common set of
  visualization tools at the outset could streamline the process and ensure
  consistency across team members.
  - **Dedicated time for interpretation:** Allocate specific time slots for
  discussing and interpreting findings as a team, ensuring a shared understanding
  of the insights and their implications.

- **Lessons Learned**:
  - **Analysis is an art and a science:** While algorithms provide the science,
  the art lies in asking the right questions, interpreting results critically,
  and effectively communicating insights.
  - **The power of visualization:** Effective data visualization
  is not just about pretty graphs; it's a powerful tool for discovery,
  communication, and identifying data quality issues.
  - **Model interpretability matters:** For initial insights, simpler,
  interpretable models can often provide more immediate value than complex
  black-box models, especially when trying to understand underlying relationships.

## Individual Retrospectives

### Caesar

I made some big changes on one commit, and it made some difficulties,
so i learned to make more commits along the way to avoid big conflicts.

### Fahed

Through this milestone, I experienced the full data science workflow from raw data
processing to actionable insights. The most valuable learning was developing
professional skepticism in machine learning - when our initial models showed
perfect accuracy, instead of celebrating, I investigated and discovered data
leakage issues. This taught me that critical thinking is just as important as
technical skills in data science.

Working with log records and transforming them into meaningful features
was both challenging and rewarding. I learned to balance technical complexity with
practical constraints - sometimes simpler, interpretable models provide more value
than complex algorithms, especially when stakeholders need to
understand and act on the results.

The systematic approach to EDA (univariate, bivariate, multivariate) helped me
build confidence in statistical findings rather than just impressive-looking
results. This structured methodology will be valuable in future data science
projects where thoroughness and validity matter more than flashy metrics.

---
