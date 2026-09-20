import streamlit as st

st.set_page_config(
    page_title="Travel Assistant",
    page_icon="✈️",
    layout="wide"
)

# ---------- CUSTOM STYLE ----------
st.markdown("""
<style>
    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #777;
        font-size: 17px;
        margin-bottom: 30px;
    }

    .trip-card {
        padding: 25px;
        border-radius: 18px;
        background: #f7f9fc;
        border: 1px solid #e5e7eb;
        margin-top: 20px;
    }

    .budget-card {
        padding: 20px;
        border-radius: 15px;
        background: #ffffff;
        border: 1px solid #e5e7eb;
        text-align: center;
    }

    .total-card {
        padding: 25px;
        border-radius: 18px;
        background: #eef7ff;
        border: 1px solid #cfe8ff;
        text-align: center;
        margin-top: 20px;
    }

    .total-price {
        font-size: 32px;
        font-weight: 700;
    }

    .day-card {
        padding: 16px 20px;
        border-radius: 14px;
        background: #f8fafc;
        border: 1px solid #e5e7eb;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)


# ---------- HEADER ----------

st.markdown(
    '<div class="main-title">✈️ Travel Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Plan your trip, estimate your budget and get a simple day-wise itinerary.</div>',
    unsafe_allow_html=True
)

# ---------- INPUT SECTION ----------

st.subheader("📝 Plan Your Trip")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("👤 Your Name")

    starting_location = st.text_input(
        "📍 Starting Location",
        placeholder="e.g. Amravati"
    )

    destination = st.selectbox(
        "🌍 Destination",
        ["Goa", "Mumbai", "Delhi", "Pune"]
    )

with col2:
    days = st.number_input(
        "📅 Number of Days",
        min_value=1,
        max_value=30,
        value=4
    )

    budget = st.number_input(
        "💰 Your Budget (₹)",
        min_value=1000,
        value=10000,
        step=500
    )

    travel_preference = st.selectbox(
        "🚗 Travel Preference",
        ["Budget", "Comfort", "Premium"]
    )


st.write("")

plan_button = st.button(
    "✈️ Plan My Trip",
    use_container_width=True
)


# ---------- CALCULATION ----------

if plan_button:

    if name.strip() == "" or starting_location.strip() == "":
        st.warning("Please enter your name and starting location.")

    else:

        if travel_preference == "Budget":
            hotel_per_day = 1000
            food_per_day = 500
            transport_per_day = 600

        elif travel_preference == "Comfort":
            hotel_per_day = 1800
            food_per_day = 800
            transport_per_day = 1000

        else:
            hotel_per_day = 3000
            food_per_day = 1200
            transport_per_day = 1800

        hotel_cost = hotel_per_day * days
        food_cost = food_per_day * days
        transport_cost = transport_per_day * days

        total_cost = hotel_cost + food_cost + transport_cost

        # ---------- TRIP SUMMARY ----------

        st.divider()

        st.subheader("✈️ YOUR TRIP")

        st.markdown(
            f"""
            <div class="trip-card">
                <h2>{name} → {destination}</h2>
                <p>📍 Starting from <b>{starting_location}</b></p>
                <p>📅 <b>{days} Days</b></p>
                <p>🚗 Travel Style: <b>{travel_preference}</b></p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # ---------- BUDGET ----------

        st.write("")
        st.subheader("💰 Estimated Budget")

        b1, b2, b3 = st.columns(3)

        with b1:
            st.markdown(
                f"""
                <div class="budget-card">
                    <h3>🏨 Hotel</h3>
                    <h2>₹{hotel_cost:,}</h2>
                </div>
                """,
                unsafe_allow_html=True
            )

        with b2:
            st.markdown(
                f"""
                <div class="budget-card">
                    <h3>🍔 Food</h3>
                    <h2>₹{food_cost:,}</h2>
                </div>
                """,
                unsafe_allow_html=True
            )

        with b3:
            st.markdown(
                f"""
                <div class="budget-card">
                    <h3>🚗 Transport</h3>
                    <h2>₹{transport_cost:,}</h2>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown(
            f"""
            <div class="total-card">
                <p>💰 TOTAL ESTIMATED BUDGET</p>
                <div class="total-price">₹{total_cost:,}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # ---------- BUDGET CHECK ----------

        st.write("")

        if total_cost <= budget:
            st.success(
                f"✅ Your estimated trip cost is within your ₹{budget:,} budget."
            )
        else:
            st.warning(
                f"⚠️ Estimated cost is ₹{total_cost:,}, which is above your ₹{budget:,} budget."
            )

        # ---------- ITINERARY ----------

        st.divider()

        st.subheader("🗓️ Suggested Plan")

        for day in range(1, days + 1):

            if day == 1:
                activity = "Arrival + Local Exploration"
                emoji = "🛬"

            elif day == days:
                activity = "Departure + Last-minute Sightseeing"
                emoji = "🧳"

            elif day == 2:
                activity = "Sightseeing + Famous Attractions"
                emoji = "📸"

            else:
                activity = "Adventure + Local Experiences"
                emoji = "🏝️"

            st.markdown(
                f"""
                <div class="day-card">
                    <b>{emoji} Day {day}</b>
                    <br>
                    {activity}
                </div>
                """,
                unsafe_allow_html=True
            )

        # ---------- DISCLAIMER ----------

        st.write("")

        st.info(
            "Prices shown are estimated costs for demonstration purposes. "
            "They are not live hotel, food or transport prices. "
            "Actual costs may vary."
        )

        st.success("✈️ Have a great journey!")