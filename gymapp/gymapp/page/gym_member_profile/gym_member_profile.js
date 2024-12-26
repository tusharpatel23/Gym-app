frappe.pages['gym-member-profile'].on_page_load = function (wrapper) {
    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Member Profile',
        single_column: true
    });

    frappe.call({
        method: "gymapp.gymapp.page.gym_member_profile.gym_member_profile.get_member_data",
        args: {
            member: frappe.session.user
        },
        callback: function (r) {
            if (r.message) {
                let member_data = r.message;

                $(wrapper).html(`
                    <div class="profile-container">
                        <div class="plan">
                            <img src="${member_data.img}" alt="Profile Image" class="profile-image">
                            <h2>Welcome, ${member_data.member_name}</h2>
                    
                            <p class = "heading">Here are your details and plan:</p>
                            <p><b>Active Plan:</b> ${member_data.active_plan}</p>
                            <p><b>Gym Join Date:</b> ${member_data.start_date}</p>
                            <p><b>Remaining Days:</b> ${member_data.remaining_days}</p>
                            <p><b>Gym Amount:</b> ${member_data.gym_amount}</p>
                        </div>

                        <div class ="sub">
                            <p class="heading">Here are your subscription details:</p>
                            <p><b>Trainer Name:</b> ${member_data.trainer_name}</p>
                            <p><b>Sub Start:</b> ${member_data.sub_start}</p>
                            <p><b>Remaining Day:</b> ${member_data.sub_remaining_day}</p>
                            <p><b>Total Hours:</b> ${member_data.total_hours}</p>
                            <p><b>Total Rate:</b> ${member_data.total_rate}</p>
                            

                        </div>

                        <div class="button-container">
                            <button id="btn-book-locker" class="btn-bookLocker">Book Locker</button>
                            <button id="btn-trainer-subscription" class="btn-trainerSubscription">Trainer Subscription</button>
                            <button id="btn-book-class" class="btn-bookClass">Book Class</button>
                        </div>
                    </div>
                `);

                $('#btn-book-locker').click(function () {
                    window.location.href = 'http://192.168.167.121:8003/locker-booking/new';
                });

                $('#btn-trainer-subscription').click(function () {
                    window.location.href = 'http://192.168.167.121:8003/trainer-subscription-form/new';
                });

                $('#btn-book-class').click(function () {
                    window.location.href = 'http://192.168.167.121:8003/book-class/new';
                });
            }
        }
    });
};
