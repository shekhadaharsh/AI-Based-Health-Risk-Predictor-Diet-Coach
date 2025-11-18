# diet/diet_plan.py

def get_diet_plan(bmi, activity, disease, diet_pref):
    plan = {}

    # --- BMI based breakfast ---
    if bmi < 18.5:  # Underweight
        plan["Breakfast"] = "High-calorie: Peanut butter toast, banana shake, boiled eggs"
    elif 18.5 <= bmi < 24.9:  # Normal
        plan["Breakfast"] = "Balanced: Oats with fruits, milk, boiled egg/soya"
    else:  # Overweight/Obese
        plan["Breakfast"] = "Low-calorie: Green tea, vegetable upma, sprouts"

    # --- Activity level based lunch ---
    if activity == 0:  # sedentary
        plan["Lunch"] = "Light: 1 chapati, dal, cucumber salad"
    elif activity == 1:  # moderate
        plan["Lunch"] = "Moderate: 2 chapati, brown rice, paneer/chicken, salad"
    else:  # high active
        plan["Lunch"] = "Energy-rich: Quinoa, grilled chicken/fish, veggies, curd"

    # --- Dinner customization based on disease ---
    if disease == 1:  # history of disease
        plan["Dinner"] = "Very light: Clear soup, 1 roti, boiled veggies, no fried food"
    else:
        plan["Dinner"] = "Normal: 2 chapati, sabzi, curd, light dal"

    # --- Diet preference filter ---
    if diet_pref == 0:  # Veg
        plan = {meal: item.replace("chicken/fish", "paneer/soya") for meal, item in plan.items()}
    elif diet_pref == 2:  # Vegan
        plan = {meal: item.replace("milk", "almond milk")
                        .replace("curd", "soy curd")
                        .replace("paneer", "tofu") for meal, item in plan.items()}

    return plan
