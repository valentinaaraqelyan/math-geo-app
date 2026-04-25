import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, Circle, Polygon
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

st.set_page_config(page_title="Երկրաչափական Հաշվիչ", page_icon="📐", layout="wide")


# CSS՝ վերնագիրը հեռախոսի էկրանին հարմարեցնելու համար
st.markdown("""
    <style>
    .main-title {
        font-size: 28px !important;
        font-weight: bold;
        text-align: center;
        color: #1E3A8A;
        line-height: 1.2;
    }
    @media (max-width: 600px) {
        .main-title {
            font-size: 20px !important;
        }
    }
    </style>
    <div class="main-title">📐 Երկրաչափական Հաշվիչ</div>
    """, unsafe_allow_html=True)

main_choice = st.sidebar.radio("Ընտրեք բաժինը", ["Գլխավոր", "ՀԱՐԹԱՉԱՓՈՒԹՅՈՒՆ", "ՏԱՐԱԾԱՉԱՓՈՒԹՅՈՒՆ"])

# --- 2D ԲԱԺԻՆ ---
if main_choice == "ՀԱՐԹԱՉԱՓՈՒԹՅՈՒՆ":
    shape = st.selectbox("Ընտրեք պատկերը", ["Ուղղանկյուն", "Քառակուսի", "Եռանկյուն", "Ուղղանկյուն եռանկյուն", "Շեղանկյուն", "Շրջան", "Զուգահեռագիծ", "Սեղան"])
    fig, ax = plt.subplots(figsize=(5, 4))
    
    if shape == "Ուղղանկյուն":
        a, b = st.number_input("Կողմ A", 0.1, value=5.0), st.number_input("Կողմ B", 0.1, value=3.0)
        st.success(f"Մակերես: {a*b:.2f} | Պարագիծ: {2*(a+b):.2f}")
        ax.add_patch(Rectangle((0, 0), a, b, color='skyblue', ec='blue', alpha=0.6))
        ax.set_xlim(-1, a+1); ax.set_ylim(-1, b+1)

    elif shape == "Քառակուսի":
        a = st.number_input("Կողմը", 0.1, value=4.0)
        st.success(f"Մակերես: {a**2:.2f} | Պարագիծ: {4*a:.2f}")
        ax.add_patch(Rectangle((0, 0), a, a, color='lightgreen', ec='green', alpha=0.6))
        ax.set_xlim(-1, a+1); ax.set_ylim(-1, a+1)

    elif shape == "Եռանկյուն":
        a, h = st.number_input("Հիմքը", 0.1, value=6.0), st.number_input("Բարձրությունը", 0.1, value=4.0)
        st.success(f"Մակերես: {0.5*a*h:.2f}")
        ax.add_patch(Polygon([[0,0], [a,0], [a/2, h]], color='orange', ec='red', alpha=0.6))
        ax.set_xlim(-1, a+1); ax.set_ylim(-1, h+1)

    elif shape == "Ուղղանկյուն եռանկյուն":
        a, b = st.number_input("Էջ A", 0.1, value=3.0), st.number_input("Էջ B", 0.1, value=4.0)
        st.success(f"Մակերես: {0.5*a*b:.2f} | Ներքնաձիգ: {math.sqrt(a**2+b**2):.2f}")
        ax.add_patch(Polygon([[0,0], [a,0], [0, b]], color='cyan', ec='blue', alpha=0.6))
        ax.set_xlim(-1, a+1); ax.set_ylim(-1, b+1)

    elif shape == "Շեղանկյուն":
        d1, d2 = st.number_input("Անկյունագիծ 1", 0.1, 6.0), st.number_input("Անկյունագիծ 2", 0.1, 8.0)
        st.success(f"Մակերես: {(d1*d2)/2:.2f}")
        ax.add_patch(Polygon([[d1/2, 0], [d1, d2/2], [d1/2, d2], [0, d2/2]], color='purple', alpha=0.5))
        ax.set_xlim(-1, d1+1); ax.set_ylim(-1, d2+1)

    elif shape == "Շրջան":
        r = st.number_input("Շառավիղը", 0.1, 3.0)
        st.success(f"Մակերես: {math.pi*r**2:.2f}")
        ax.add_patch(Circle((0, 0), r, color='pink', ec='red', alpha=0.6))
        ax.set_xlim(-r-1, r+1); ax.set_ylim(-r-1, r+1)

    elif shape == "Զուգահեռագիծ":
        a, h = st.number_input("Հիմքը", 0.1, 6.0), st.number_input("Բարձրությունը", 0.1, 4.0)
        st.success(f"Մակերես: {a*h:.2f}")
        ax.add_patch(Polygon([[0,0], [a, 0], [a+1, h], [1, h]], color='gold', alpha=0.6))
        ax.set_xlim(-1, a+2); ax.set_ylim(-1, h+1)

    elif shape == "Սեղան":
        a, b, h = st.number_input("Հիմք 1", 0.1, 8.0), st.number_input("Հիմք 2", 0.1, 5.0), st.number_input("Բարձրություն", 0.1, 4.0)
        st.success(f"Մակերես: {((a+b)/2)*h:.2f}")
        ax.add_patch(Polygon([[0,0], [a,0], [(a+b)/2+1, h], [(a-b)/2+1, h]], color='grey', alpha=0.5))
        ax.set_xlim(-1, a+2); ax.set_ylim(-1, h+1)

    ax.set_aspect('equal'); ax.grid(True, linestyle='--', alpha=0.5)
    st.pyplot(fig)

# --- 3D ԲԱԺԻՆ ---
elif main_choice == "ՏԱՐԱԾԱՉԱՓՈՒԹՅՈՒՆ":
    body = st.selectbox("Ընտրեք մարմինը", ["Ուղղանկյունանիստ", "Խորանարդ", "Բուրգ", "Գլան", "Կոն", "Գունդ"])
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111, projection='3d')
    
    if body == "Ուղղանկյունանիստ":
        a, b, c = st.number_input("Երկարություն", 0.1, 5.0), st.number_input("Լայնություն", 0.1, 3.0), st.number_input("Բարձրություն", 0.1, 4.0)
        st.success(f"Ծավալ: {a*b*c:.2f}")
        ax.bar3d(0, 0, 0, a, b, c, color='skyblue', alpha=0.5)

    elif body == "Խորանարդ":
        a = st.number_input("Կողմը", 0.1, 3.0)
        st.success(f"Ծավալ: {a**3:.2f}")
        ax.bar3d(0, 0, 0, a, a, a, color='lightgreen', alpha=0.5)

    elif body == "Բուրգ":
        a, h = st.number_input("Հիմքի կողմը", 0.1, 4.0), st.number_input("Բարձրությունը", 0.1, 5.0)
        st.success(f"Ծավալ: {(1/3)*a**2*h:.2f}")
        v = np.array([[0,0,0], [a,0,0], [a,a,0], [0,a,0], [a/2,a/2,h]])
        faces = [[v[0],v[1],v[4]], [v[1],v[2],v[4]], [v[2],v[3],v[4]], [v[3],v[0],v[4]], [v[0],v[1],v[2],v[3]]]
        ax.add_collection3d(Poly3DCollection(faces, facecolors='orange', linewidths=1, edgecolors='r', alpha=.4))
        ax.set_xlim(0, a); ax.set_ylim(0, a); ax.set_zlim(0, h)

    elif body == "Գլան":
        r, h = st.number_input("Շառավիղ", 0.1, 2.0), st.number_input("Բարձրություն", 0.1, 5.0)
        st.success(f"Ծավալ: {math.pi*r**2*h:.2f}")
        z = np.linspace(0, h, 20); theta = np.linspace(0, 2*np.pi, 20)
        theta_grid, z_grid = np.meshgrid(theta, z)
        ax.plot_surface(r*np.cos(theta_grid), r*np.sin(theta_grid), z_grid, color='cyan', alpha=0.5)

    elif body == "Կոն":
        r, h = st.number_input("Շառավիղ", 0.1, 2.0), st.number_input("Բարձրություն", 0.1, 5.0)
        st.success(f"Ծավալ: {(1/3)*math.pi*r**2*h:.2f}")
        z = np.linspace(0, h, 20); theta = np.linspace(0, 2*np.pi, 20)
        theta_grid, z_grid = np.meshgrid(theta, np.linspace(0, 1, 20))
        ax.plot_surface(r*z_grid*np.cos(theta_grid), r*z_grid*np.sin(theta_grid), h*(1-z_grid), color='magenta', alpha=0.5)

    elif body == "Գունդ":
        r = st.number_input("Շառավիղը", 0.1, 3.0)
        st.success(f"Ծավալ: {(4/3)*math.pi*r**3:.2f}")
        u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:20j]
        ax.plot_surface(r*np.cos(u)*np.sin(v), r*np.sin(u)*np.sin(v), r*np.cos(v), color="yellow", alpha=0.6)

    st.pyplot(fig)

else:
    st.write("### Բարի գալուստ:")
    st.write("Ձախ անկյունի մենյուից ընտրեք երկրաչափության հետաքրքրող բաժինը")
