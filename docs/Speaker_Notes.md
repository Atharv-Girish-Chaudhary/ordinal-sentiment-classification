# Speaker Notes: Ordinal vs Nominal Sentiment Classification
## Final Project Presentation (~7 minutes)

---

## SLIDE 1: Title (20 seconds)

**[Don't read the slide - just introduce yourselves]**

> "Hi everyone, we're [Name], [Name], and [Name], and today we're presenting our comparative study on sentiment classification — specifically, whether ordinal methods can outperform traditional nominal approaches when analyzing Amazon product reviews."

**Transition:** "Let's start with why this problem matters."

---

## SLIDE 2: Why Sentiment Classification Matters (45 seconds)

**[Point to the scale/business sections as you speak]**

> "Every day, millions of product reviews are posted across e-commerce platforms. Businesses use these reviews for customer satisfaction monitoring, product improvements, and brand reputation tracking."

**[Point to the critical gap section]**

> "But here's the problem: most machine learning systems treat ALL classification errors equally. They see predicting 1-star for a 5-star review as the same mistake as predicting 4-star for a 5-star review."

**[Point to the real-world impact box]**

> "Imagine a customer writes a glowing 5-star review saying 'I absolutely love this product' — and the system predicts 1-star. That customer might receive an unnecessary apology email, business decisions get skewed by bad data, and trust is damaged."

**[Point to research question]**

> "So our research question is: Can ordinal methods — methods that respect the natural ordering of star ratings — reduce these severe, catastrophic errors?"

**Transition:** "To answer this, let's look at our dataset."

---

## SLIDE 3: Data Analysis - Class Distribution (50 seconds)

**[Point to the bar chart]**

> "We used the Amazon Electronics Reviews dataset from McAuley Lab at UCSD — about 50,000 reviews total."

**[Point to the severe imbalance box]**

> "The first thing we discovered is a severe class imbalance. There's a 14.3 to 1 ratio between 5-star and 2-star reviews. Over 60% of reviews are 5-star, while the minority classes — 1, 2, and 3-star — make up only about 17% combined."

**[Point to class breakdown]**

> "This imbalance is a major challenge because models tend to predict the majority class and struggle with minority classes."

**[Point to dataset statistics]**

> "We split the data 80-20 for training and testing, using stratified sampling to preserve these proportions in both sets."

**Transition:** "Beyond class distribution, we also analyzed the features."

---

## SLIDE 4: Feature Discovery - Word Analysis (45 seconds)

**[Point to the feature importance chart]**

> "This chart shows the top 20 features for predicting 5-star reviews using Logistic Regression coefficients."

**[Point to top 5-star words box]**

> "As expected, positive sentiment words dominate: 'great,' 'love,' 'perfect,' 'excellent,' 'amazing' — these are strong indicators of high ratings."

**[Point to top 1-star words box]**

> "For 1-star reviews, we see words like 'return,' 'waste,' 'broke,' 'terrible,' and 'money' — words associated with product failures and disappointment."

**[Point to key discovery box]**

> "A key discovery was that bigrams — two-word phrases — capture negation patterns that unigrams miss. For example, 'not good' versus just 'good' have opposite meanings."

**[Point to feature selection box]**

> "Based on this, we used TF-IDF vectorization with 5,000 features including both unigrams and bigrams."

**Transition:** "Now let me hand it over to [Next Speaker] to discuss our methodology."

---

## SLIDE 5: Related Work (45 seconds)

**[Point to left paper - Pang & Lee]**

> "Our work builds on two foundational papers. First, Pang and Lee's 2008 survey established machine learning approaches for sentiment analysis using Naive Bayes and SVM. However, they treated sentiment as binary — positive or negative — ignoring the ordinal structure of star ratings."

> "We validated their finding that Logistic Regression outperforms Naive Bayes — we got 65.95% versus 63.12% accuracy."

**[Point to right paper - McCullagh]**

> "Second, McCullagh's 1980 paper introduced the proportional odds model for ordinal regression. This models cumulative probabilities — the probability that Y is less than or equal to k — which respects the ordering of categories."

> "We validated this approach too: ordinal methods reduced our severe error rate by 48%."

**Transition:** "Let me walk you through our data processing pipeline."

---

## SLIDE 6: Data Processing Pipeline (50 seconds)

**[Point to the pipeline flow at top]**

> "Our pipeline has four main stages: preprocessing, TF-IDF vectorization, label encoding, and train-test split."

**[Point to Step 1]**

> "First, text preprocessing: we convert to lowercase, remove punctuation, and filter stopwords. So 'GREAT product!!' becomes simply 'great product'."

**[Point to Step 2]**

> "Second, TF-IDF vectorization weights terms by their importance in a document relative to the corpus. We extract 5,000 features using both unigrams and bigrams."

**[Point to Step 3 - this is KEY]**

> "Third — and this is crucial — label encoding. Nominal encoding treats ratings as unordered categories: 1-star equals class A, 2-star equals class B, with no relationship between them. Ordinal encoding preserves the order: 1 is less than 2 is less than 3, and so on. This lets models learn that adjacent ratings are similar."

**[Point to Step 4]**

> "Finally, we split 80-20 with stratified sampling, giving us about 40,000 training and 10,000 test samples."

**Transition:** "Now let's look at the four models we compared."

---

## SLIDE 7: Learning Algorithms (55 seconds)

**[Point to Nominal header]**

> "We tested two nominal approaches that treat ratings as unordered categories."

**[Point to Naive Bayes]**

> "Multinomial Naive Bayes calculates the probability of each class given the text using Bayes' theorem. It's fast and works well with sparse text data, but assumes feature independence."

**[Point to Logistic Regression]**

> "Logistic Regression with softmax gives calibrated class probabilities. It's interpretable and handles high-dimensional data well. But critically, it penalizes all errors equally."

**[Point to Ordinal header]**

> "Our ordinal approaches respect the natural ordering of ratings."

**[Point to Ridge Regression]**

> "Ridge Regression treats ratings as continuous numbers and minimizes squared error. This is key: a 4-class error — predicting 1 for a 5 — gets penalized 16 times more than a 1-class error, because the squared difference is 16 versus 1."

**[Point to Ordinal Logistic]**

> "Ordinal Logistic Regression learns K-1 thresholds between classes, modeling cumulative probabilities."

**[Point to bottom comparison]**

> "The fundamental difference: nominal methods see all errors as equally wrong, while ordinal methods understand that some errors are much worse than others."

**Transition:** "Now [Next Speaker] will show you our results."

---

## SLIDE 8: Results (50 seconds)

**[Point to confusion matrices]**

> "These confusion matrices show predictions versus actual ratings for all four models. The diagonal represents correct predictions — we want high values there. Off-diagonal values are errors."

**[Point to results table]**

> "Looking at our metrics: Logistic Regression wins on accuracy at 66%, but look at the severe error column. Naive Bayes has 44% severe errors — almost half its predictions are catastrophically wrong!"

**[Point to Ridge row - emphasize this]**

> "Ridge Regression only gets 50% accuracy, but its severe error rate is just 18.1% — less than half of the nominal methods."

**[Point to Why LR Wins box]**

> "Logistic Regression wins accuracy because softmax optimizes for exact matches, and the clear vocabulary differences between ratings help."

**[Point to Why Ridge Wins box]**

> "But Ridge wins on severe errors because squared error loss heavily penalizes distant predictions. When Ridge is wrong, the errors cluster near the diagonal — they're 'close misses' rather than disasters."

**Transition:** "This leads to our key finding."

---

## SLIDE 9: Key Finding (35 seconds)

**[Let the visual speak - pause for effect]**

> "Here's our main result: a 48% reduction in severe misclassifications."

**[Point to the two boxes]**

> "The nominal methods average 39.6% severe error rate. Ridge Regression achieves just 18.1%."

**[Point to explanation at bottom]**

> "Why does this work? Ordinal encoding teaches the model that adjacent ratings are more similar. When the model makes mistakes, they tend to be close misses — predicting 4 instead of 5 — rather than catastrophic errors like predicting 1 instead of 5."

> "For customer-facing applications, this difference is huge."

**Transition:** "So what did we learn from this project?"

---

## SLIDE 10: What We Learned (50 seconds)

**[Point to each box as you discuss it]**

> "First: ordinal structure matters. Star ratings have inherent order that standard classifiers ignore. Respecting this order reduces severe errors by 48%."

> "Second: accuracy isn't everything. High accuracy can hide catastrophic errors. Logistic Regression gets 66% accuracy but still makes severe errors 35% of the time. For ordinal tasks, you need to evaluate error severity, not just accuracy."

> "Third: class imbalance is challenging. That 14-to-1 ratio really hurts minority class performance. All our models struggled with 2-star and 3-star reviews, with F1 scores below 0.20. Future work could explore SMOTE or cost-sensitive learning."

> "Fourth: trade-offs require context. There's no single best model. Use Ridge when you need to minimize severe errors — like customer service routing. Use Logistic Regression when you need exact classification."

**[Point to research question answer]**

> "So to answer our research question: Yes, ordinal methods absolutely justify their complexity when minimizing severe errors is the priority."

**Transition:** "And that concludes our presentation."

---

## SLIDE 11: Thank You (15 seconds)

**[Summarize quickly, then open for questions]**

> "To summarize: we analyzed nearly 50,000 reviews, compared 4 models, and achieved a 48% reduction in severe misclassification errors using ordinal methods."

> "Thank you for your attention. We're happy to take any questions."

---

# Quick Reference: Key Numbers to Remember

| Metric | Value |
|--------|-------|
| Dataset size | 49,953 reviews |
| Class imbalance | 14.3:1 (5★ vs 2★) |
| Train/Test split | 80/20 (39,962 / 9,991) |
| TF-IDF features | 5,000 |
| Best accuracy | Logistic Regression: 65.95% |
| Best severe error | Ridge Regression: 18.08% |
| Improvement | 48% reduction in severe errors |
| Severe error definition | Predictions ±2 or more classes away |

---

# Timing Checklist

| Section | Speaker | Target Time |
|---------|---------|-------------|
| Slides 1-4 | Speaker 1 | ~2:40 |
| Slides 5-7 | Speaker 2 | ~2:30 |
| Slides 8-11 | Speaker 3 | ~2:10 |
| **Total** | | **~7:20** |

---

# Presentation Tips

1. **Don't read slides** — use these notes as a guide, speak naturally
2. **Point to visuals** — reference the charts and figures as you speak
3. **Make eye contact** — look at the camera, not just your notes
4. **Smooth transitions** — use the transition phrases to hand off between speakers
5. **Practice timing** — run through at least twice before recording
6. **Speak clearly** — slightly slower than normal conversation
7. **Show enthusiasm** — you discovered something interesting, share that excitement!
