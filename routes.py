# route.py

# Define a dictionary to store the mappings
combination_to_url = {
    ('COE', '21', 'Operating Systems'): "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=117394",
    ('COE', '22', 'Operating Systems'): "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=117394",
    ('COE', '23', 'Operating Systems'): "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=117394",
    ('COE', '24', 'Operating Systems'): "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=117394",
    ('COE', '25', 'Operating Systems'): "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=117394",
    ('COE', '26', 'Operating Systems'): "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=117394",

    ('COE', '21', 'Engineering Materials'): "https://lms.thapar.edu/moodle/course/view.php?id=4239",
    ('COE', '22', 'Engineering Materials'): "https://lms.thapar.edu/moodle/course/view.php?id=4239",
    ('COE', '23', 'Engineering Materials'): "https://lms.thapar.edu/moodle/course/view.php?id=4239",
    ('COE', '24', 'Engineering Materials'): "https://lms.thapar.edu/moodle/course/view.php?id=4239",
    ('COE', '25', 'Engineering Materials'): "https://lms.thapar.edu/moodle/course/view.php?id=4239",
    ('COE', '26', 'Engineering Materials'): "https://lms.thapar.edu/moodle/course/view.php?id=4239",

    ('ENC', '5', 'Engineering Materials'): "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=114921",
    ('ENC', '6', 'Engineering Materials'): "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=114921",
    ('ENC', '7', 'Engineering Materials'): "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=114921",
    ('ENC', '8', 'Engineering Materials'): "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=114921",

    ('ENC', '1', 'Engineering Materials'): "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=114919",
    ('ENC', '2', 'Engineering Materials'): "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=114919",
    ('ENC', '3', 'Engineering Materials'): "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=114919",
    ('ENC', '4', 'Engineering Materials'): "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=114919",

    ('ECE', '1', 'Engineering Materials'): "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=114885",
    ('ECE', '1', 'Engineering Materials'): "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=114885",
    ('ECE', '1', 'Engineering Materials'): "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=114885",
    ('ECE', '1', 'Engineering Materials'): "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=114885",

    ('BT', '1', 'BIOPHYSICS AND BIOMATERIALS'): "https://lms.thapar.edu/moOdle/mod/attendance/view.php?id=114966",
    ('BT', '2', 'BIOPHYSICS AND BIOMATERIALS'): "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=114966",
    ('BT', '3', 'BIOPHYSICS AND BIOMATERIALS'): "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=114966",
    ('BT', '4', 'BIOPHYSICS AND BIOMATERIALS'): "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=114966",

}


def determine_target_url(branch, subgroup, course_name):
    # Create a tuple representing the combination
    combination = (branch, subgroup, course_name)

    # Check if the combination exists in the dictionary
    if combination in combination_to_url:
        return combination_to_url[combination]
    else:
        return "https://google.com"  # Default URL

