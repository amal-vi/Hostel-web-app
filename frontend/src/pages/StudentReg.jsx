import React from "react";
import styles from "../pages/StudentReg.module.css";

function StudentReg() {
  return (
    <>
        <h2 className={styles.h2}>Student Registration</h2>
        <form
          className={styles.form}
          action="{{ url_for('auth.registrationStudents') }}"
          method="POST"
        >
          <label className={styles.label}>Full Name</label>
          <input
            className={styles.input}
            type="text"
            name="full_name"
            required=""
          />
          <label className={styles.label}>Email</label>
          <input
            className={styles.input}
            type="email"
            name="email"
            required=""
          />
          <label className={styles.label}>Phone Number</label>
          <input
            className={styles.input}
            type="text"
            name="phone_number"
            required=""
          />
          <label className={styles.label}>Date of Birth</label>
          <input
            className={styles.input}
            type="date"
            name="date_of_birth"
            required=""
          />
          <label className={styles.label}>Address</label>
          <textarea
            className={styles.textarea}
            name="address"
            rows={3}
            required=""
            defaultValue={""}
          />
          <label className={styles.label}>Admission Date</label>
          <input
            className={styles.input}
            type="date"
            name="admission_date"
            required=""
          />
          <label className={styles.label}>Emergency Contact Name</label>
          <input
            className={styles.input}
            type="text"
            name="emergency_contact_name"
            required=""
          />
          <label className={styles.label}>Emergency Contact Phone</label>
          <input
            className={styles.input}
            type="text"
            name="emergency_contact_phone"
            required=""
          />
          <label className={styles.label}>Guardian Name</label>
          <input
            className={styles.input}
            type="text"
            name="guardian_name"
            required=""
          />
          <label className={styles.label}>Photo URL</label>
          <input
            className={styles.input}
            type="url"
            name="photo_url"
            required=""
          />
          <label className={styles.label}>Password</label>
          <input
            className={styles.input}
            type="password"
            name="password"
            required=""
          />
          <button className={styles.button} type="submit">
            Register
          </button>
        </form>
    </>
  );
}

export default StudentReg;
