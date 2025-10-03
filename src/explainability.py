import shap
import matplotlib.pyplot as plt
import os

def explain_model(model, X_train, output_dir="outputs/plots"):
    os.makedirs(output_dir, exist_ok=True)

    # Create SHAP explainer
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_train)

    # Summary plot
    plt.figure()
    shap.summary_plot(shap_values, X_train, show=False)
    plt.savefig(os.path.join(output_dir, "shap_summary.png"))
    plt.close()

    # Bar plot of feature importance
    plt.figure()
    shap.summary_plot(shap_values, X_train, plot_type="bar", show=False)
    plt.savefig(os.path.join(output_dir, "shap_feature_importance.png"))
    plt.close()

    print("✅ SHAP explainability plots saved!")
