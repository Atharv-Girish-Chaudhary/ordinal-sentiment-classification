# Video Presentation Script
## Ordinal vs Nominal Sentiment Classification
### Total Time: ~7 minutes (6-8 min target)

---

## Slide 1: Title Slide
**Duration: ~30 seconds**

> "Hello everyone. I'm [NAME], and along with my teammates Kien Nguyen and Zijie Liu, we're presenting our comparative study on ordinal versus nominal approaches to sentiment classification.
>
> Our project analyzes Amazon Electronics reviews to answer a fundamental question: when classifying star ratings, does it matter whether we treat them as ordered categories or just independent labels? Let's find out."

---

## Slide 2: The Challenge  
**Duration: ~45 seconds**

> "Here's the core problem we're addressing. Star ratings have an inherent ordinal structure—a 1-star review represents worse sentiment than a 2-star, which is worse than a 3-star, and so on.
>
> But most classification algorithms treat these ratings as unordered categories. Under this nominal view, predicting 1-star when the true rating is 5-stars is treated the same as predicting 4-stars—both are just 'wrong.'
>
> But intuitively, we know predicting 1 when the answer is 5 is a much more severe error than predicting 4 when the answer is 5. That's a 4-class error versus a 1-class error. This is the gap our research addresses."

---

## Slide 3: Research Question
**Duration: ~40 seconds**

> "This leads us to our central research question: Do performance gains from treating star ratings as ordinal justify the increased model complexity?
>
> We break this down into three sub-questions. First, how do ordinal methods compare on standard metrics like accuracy? Second, do they actually reduce severe misclassifications? And third, what are the practical trade-offs for real-world applications?
>
> By the end of this presentation, we'll have clear answers to all three."

---

## Slide 4: Related Work
**Duration: ~45 seconds**

> "Our work builds on two foundational contributions in the field.
>
> First, Pang and Lee's seminal 2008 survey on Opinion Mining and Sentiment Analysis established machine learning approaches for sentiment classification. They demonstrated that Naive Bayes and Support Vector Machines could effectively classify movie reviews. However, their work treated sentiment as binary—positive or negative—ignoring the ordinal structure of star ratings.
>
> Second, McCullagh's 1980 paper introduced the proportional odds model for ordinal regression. This approach models cumulative probabilities with learned thresholds, properly respecting the ordered nature of categories.
>
> Our work bridges these two lines of research: we compare traditional nominal sentiment methods against ordinal regression techniques on star rating prediction."

---

## Slide 5: Dataset Overview
**Duration: ~45 seconds**

> "For our study, we used the Amazon Electronics Reviews dataset from the McAuley Lab at UCSD. After cleaning, we have nearly 50,000 reviews with star ratings from 1 to 5.
>
> We split the data 80-20 for training and testing, using about 40,000 samples for training and 10,000 for evaluation.
>
> One critical challenge you can see in this distribution chart: we have severe class imbalance. 5-star reviews dominate with over 30,000 samples, while 2-star reviews have only about 2,100—that's a 14 to 1 ratio. The minority classes, 1 through 3 stars, represent only 17% of our data. This imbalance affects all our models."

---

## Slide 6: Methodology
**Duration: ~50 seconds**

> "Our methodology follows a standard text classification pipeline. We start with preprocessing—lowercasing, removing punctuation, and filtering stopwords. Then we convert text to features using TF-IDF vectorization with up to 5,000 features, including both unigrams and bigrams.
>
> For nominal models, we use standard one-hot encoding where each rating is an independent category. For ordinal models, we encode labels as integers 1 through 5, preserving their natural order.
>
> We evaluate using three metrics. Accuracy gives us overall correctness. Mean Absolute Error tells us the average distance between predictions and true ratings. And our key metric—severe error rate—measures how often we make predictions that are 3 or more classes away from the truth. This captures catastrophic misclassifications."

---

## Slide 7: Models Compared
**Duration: ~50 seconds**

> "We compared four models, two nominal and two ordinal.
>
> On the nominal side, we have Multinomial Naive Bayes—a fast, simple probabilistic baseline that works well with word frequencies. And Logistic Regression with softmax, which is interpretable and regularized but ignores class ordering.
>
> On the ordinal side, we have Ridge Regression, which treats ratings as continuous values with L2 regularization, then rounds predictions to the nearest class. This approach naturally penalizes predictions far from the true value. We also have Ordinal Logistic Regression, also called the proportional odds model, which learns optimal thresholds between adjacent classes.
>
> Each model has trade-offs between simplicity, accuracy, and respecting the ordinal structure."

---

## Slide 8: Results Comparison
**Duration: ~50 seconds**

> "Now for our results. Looking at this table, we see some interesting patterns.
>
> For accuracy, Logistic Regression wins at 65.95%, followed closely by Ordinal Logistic at 65.86%. Ridge Regression lags behind at only 50.29%.
>
> For Mean Absolute Error, Logistic Regression again leads with 0.534, meaning predictions are on average about half a star away from truth.
>
> But here's where it gets interesting—look at severe error rate. Ridge Regression achieves only 18.08% severe errors, while Naive Bayes has 44.37%. That's a dramatic difference.
>
> The pattern is clear: nominal methods win on accuracy, but ordinal methods, especially Ridge Regression, dramatically reduce severe errors."

---

## Slide 9: Key Finding
**Duration: ~40 seconds**

> "This brings us to our key finding. Ridge Regression achieved a 48% reduction in severe errors compared to the nominal average.
>
> The nominal methods averaged about 39.6% severe error rate. Ridge Regression brought that down to just 18.1%.
>
> What this means practically: ordinal encoding teaches the model that adjacent ratings are similar. When Ridge makes mistakes, it tends to predict 4 when the answer is 5, rather than predicting 1 when the answer is 5. The errors cluster closer to the diagonal of the confusion matrix.
>
> This is the core trade-off: you sacrifice some exact accuracy to dramatically reduce catastrophic misclassifications."

---

## Slide 10: Conclusions
**Duration: ~50 seconds**

> "Let's summarize our key takeaways.
>
> First, ordinal encoding significantly reduces severe errors—Ridge Regression achieved 48% fewer catastrophic misclassifications than nominal methods.
>
> Second, nominal methods still excel at raw accuracy—Logistic Regression achieved the highest overall accuracy at nearly 66%.
>
> Third, class imbalance limits all models—minority classes had poor F1 scores across the board, which is a challenge for future work.
>
> So when should you use each approach? Use ordinal methods when severe errors are costly—for customer experience monitoring, satisfaction tracking, or anywhere a wildly wrong prediction causes real harm. Use nominal methods when exact classification matters and all errors are equally bad.
>
> To answer our research question: Yes, ordinal methods justify their complexity when minimizing severe errors is your priority."

---

## Slide 11: Thank You
**Duration: ~20 seconds**

> "To summarize our study: we analyzed nearly 50,000 reviews, compared 4 models, and found that ordinal encoding can reduce severe errors by 48%.
>
> Thank you for your attention. We're happy to take any questions."

---

## Timing Summary

| Slide | Topic | Target Duration |
|-------|-------|-----------------|
| 1 | Title | 30 sec |
| 2 | Challenge | 45 sec |
| 3 | Research Question | 40 sec |
| 4 | Related Work | 45 sec |
| 5 | Dataset | 45 sec |
| 6 | Methodology | 50 sec |
| 7 | Models | 50 sec |
| 8 | Results | 50 sec |
| 9 | Key Finding | 40 sec |
| 10 | Conclusions | 50 sec |
| 11 | Thank You | 20 sec |
| **Total** | | **~7.5 minutes** |

---

## Recording Tips

1. **Practice 2-3 times** before recording to get comfortable with timing
2. **Speak slowly and clearly** — it's better to be slightly under time than to rush
3. **Pause briefly** between slides to let visuals sink in
4. **Emphasize key numbers**: 48% reduction, 65.95% accuracy, 18.08% severe error
5. **Use natural transitions** like "Now let's look at..." or "This brings us to..."
6. **Record in a quiet space** with good audio quality
7. **Consider screen recording software** like OBS, Zoom, or Loom
