import streamlit as st
import math

# Էջի կարգավորումներ
st.set_page_config(page_title="Երկրաչափական Հաշվիչ", page_icon="📐")

st.title("📐 Երկրաչափական Հաշվիչ")

# Sidebar մենյու
st.sidebar.header("Կառավարման վահանակ")
main_choice = st.sidebar.radio("Ընտրեք բաժինը", ["Գլխավոր", "ՀԱՐԹԱՉԱՓՈՒԹՅՈՒՆ (2D)", "ՏԱՐԱԾԱՉԱՓՈՒԹՅՈՒՆ (3D)"])

# --- ՕԺԱՆԴԱԿ ՖՈՒՆԿՑԻԱ ---
def show_result(results_dict):
    st.subheader("Արդյունքներ")
    cols = st.columns(len(results_dict))
    for i, (key, value) in enumerate(results_dict.items()):
        cols[i].metric(key, f"{value:.2f}" if isinstance(value, float) else value)

# --- ԳԼԽԱՎՈՐ ԷՋ ---
if main_choice == "Գլխավոր":
    st.write("### Մաթեմատիկա և Ծրագրավորում")
    st.write("Այս հավելվածը հանդիսանում է մեր նախագծային աշխատանքի գործնական արդյունքը։")
    st.info("Ձախ կողմի մենյուից ընտրեք բաժինը և պատկերը՝ հաշվարկները սկսելու համար։")

# --- 2D ԲԱԺԻՆ ---
elif main_choice == "ՀԱՐԹԱՉԱՓՈՒԹՅՈՒՆ (2D)":
    shape = st.selectbox("Ընտրեք պատկերը", [
        "Ուղղանկյուն", "Քառակուսի", "Եռանկյուն", "Ուղղանկյուն եռանկյուն", 
        "Շեղանկյուն", "Շրջան", "Զուգահեռագիծ", "Սեղան"
    ])
    
    if shape == "Ուղղանկյուն":
        a = st.number_input("Կողմ A", min_value=0.1, value=5.0)
        b = st.number_input("Կողմ B", min_value=0.1, value=3.0)
        show_result({"Մակերես": a*b, "Պարագիծ": 2*(a+b), "Անկյունագիծ": math.sqrt(a**2+b**2)})

    elif shape == "Քառակուսի":
        a = st.number_input("Կողմը", min_value=0.1, value=4.0)
        show_result({"Մակերես": a**2, "Պարագիծ": 4*a, "Անկյունագիծ": a*math.sqrt(2)})

    elif shape == "Եռանկյուն":
        a = st.number_input("Հիմքը", min_value=0.1, value=6.0)
        h = st.number_input("Բարձրությունը", min_value=0.1, value=4.0)
        show_result({"Մակերես": 0.5*a*h})

    elif shape == "Ուղղանկյուն եռանկյուն":
        a = st.number_input("Էջ A", min_value=0.1, value=3.0)
        b = st.number_input("Էջ B", min_value=0.1, value=4.0)
        c = math.sqrt(a**2 + b**2)
        show_result({"Մակերես": 0.5*a*b, "Ներքնաձիգ": c, "Պարագիծ": a+b+c})

    elif shape == "Շեղանկյուն":
        d1 = st.number_input("Անկյունագիծ 1", min_value=0.1, value=6.0)
        d2 = st.number_input("Անկյունագիծ 2", min_value=0.1, value=8.0)
        side = math.sqrt((d1/2)**2 + (d2/2)**2)
        show_result({"Մակերես": (d1*d2)/2, "Կողմ": side, "Պարագիծ": 4*side})

    elif shape == "Շրջան":
        r = st.number_input("Շառավիղը", min_value=0.1, value=5.0)
        show_result({"Մակերես": math.pi*r**2, "Երկարություն": 2*math.pi*r})

    elif shape == "Զուգահեռագիծ":
        a = st.number_input("Հիմքը", min_value=0.1, value=7.0)
        h = st.number_input("Բարձրությունը", min_value=0.1, value=4.0)
        show_result({"Մակերես": a*h})

    elif shape == "Սեղան":
        a = st.number_input("Հիմք 1", min_value=0.1, value=5.0)
        b = st.number_input("Հիմք 2", min_value=0.1, value=8.0)
        h = st.number_input("Բարձրությունը", min_value=0.1, value=4.0)
        show_result({"Մակերես": ((a+b)/2)*h})

# --- 3D ԲԱԺԻՆ ---
elif main_choice == "ՏԱՐԱԾԱՉԱՓՈՒԹՅՈՒՆ (3D)":
    body = st.selectbox("Ընտրեք մարմինը", [
        "Ուղղանկյունանիստ", "Խորանարդ", "Բուրգ", "Գլան", "Կոն", "Գունդ"
    ])
    
    if body == "Ուղղանկյունանիստ":
        a = st.number_input("Երկարություն", min_value=0.1, value=5.0)
        b = st.number_input("Լայնություն", min_value=0.1, value=3.0)
        c = st.number_input("Բարձրություն", min_value=0.1, value=4.0)
        show_result({"Ծավալ": a*b*c, "Կողմն. Մակերևույթ": 2*c*(a+b), "Լրիվ Մակերևույթ": 2*(a*b+b*c+a*c)})

    elif body == "Խորանարդ":
        a = st.number_input("Կողմը", min_value=0.1, value=3.0)
        show_result({"Ծավալ": a**3, "Կողմն. Մակերևույթ": 4*a**2, "Լրիվ Մակերևույթ": 6*a**2})

    elif body == "Բուրգ":
        a = st.number_input("Հիմքի կողմը", min_value=0.1, value=4.0)
        h = st.number_input("Բարձրությունը", min_value=0.1, value=6.0)
        l = math.sqrt(h**2 + (a/2)**2)
        s_side = 2 * a * l
        show_result({"Ծավալ": (1/3)*a**2*h, "Լրիվ Մակերևույթ": s_side + a**2})

    elif body == "Գլան":
        r = st.number_input("Շառավիղը", min_value=0.1, value=3.0)
        h = st.number_input("Բարձրությունը", min_value=0.1, value=7.0)
        s_side = 2*math.pi*r*h
        show_result({"Ծավալ": math.pi*r**2*h, "Լրիվ Մակերևույթ": s_side + 2*math.pi*r**2})

    elif body == "Կոն":
        r = st.number_input("Շառավիղը", min_value=0.1, value=3.0)
        h = st.number_input("Բարձրությունը", min_value=0.1, value=5.0)
        l = math.sqrt(r**2 + h**2)
        s_side = math.pi*r*l
        show_result({"Ծավալ": (1/3)*math.pi*r**2*h, "Լրիվ Մակերևույթ": s_side + math.pi*r**2})

    elif body == "Գունդ":
        r = st.number_input("Շառավիղը", min_value=0.1, value=3.0)
        show_result({"Ծավալ": (4/3)*math.pi*r**3, "Մակերևույթի մակերես": 4*math.pi*r**2})

st.sidebar.markdown("---")
