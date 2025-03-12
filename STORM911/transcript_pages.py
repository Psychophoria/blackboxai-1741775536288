from config import COLORS

FULL_SCRIPT_PAGES = [
    {
        "page_number": 0,
        "title": "Welcome to the Storm911 21 Second Pitch",
        "content_html": "Click Below To Begin The Process.",
        "buttons": [
            {
                "label": "Start",
                "color": "green",
                "function": "startScript",
                "id": "start-btn"
            }
        ]
    },
    {
        "page_number": 1,
        "title": "THE HOOK - 8.25 SECONDS",
        "content_html": (
            "Hello, is Mr. (____________________) available?<br>"
            "How are you doing today?<br>"
            "<span style='color:red; font-weight:bold;'>PAUSE AND WAIT FOR A RESPONSE!!!</span><br>"
            "I want to be honest with you,<br>"
            "this is a cold call,<br>"
            "BUT<br>"
            "if you give me 30 seconds of your time,<br>"
            "I will not waste it!<br>"
        ),
        "buttons": [
            {
                "label": "I am not Interested- 30 second objection",
                "color": "red",
                "function": "showPopup('notInterested')"
            },
            {
                "label": "I dont have time",
                "color": "red",
                "function": "showPopup('noTime')"
            },
            {
                "label": "Next",
                "color": "grey",
                "function": "nextPage",
                "id": "next-btn"
            },
            {
                "label": "End Call",
                "color": "red",
                "function": "endCallProcess"
            }
        ]
    },
    {
        "page_number": 2,
        "title": "INTRODUCTION AND APPOINTMENT SETTING",
        "content_html": (
            "My name is _______________<br>"
            "with (__________________) on a recorded line.<br>"
            "Tomorrow we will be in the area<br>"
            "giving free roof inspections<br>"
            "to some of your neighbors<br>"
            "for damages caused by the storms<br>"
            "that have hit our area,<br>"
            "and I would like to schedule an appointment with you!<br><br>"
            "Would mornings or afternoons work best for you?<br><br>"
            "<span style='color:red; font-weight:bold;'>PAUSE AND WAIT FOR A RESPONSE!!!</span><br>"
            "Thank you, let me explain the inspection process to you."
        ),
        "buttons": [
            {
                "label": "I am not Interested- 30 second objection",
                "color": "red",
                "function": "showPopup('notInterested')"
            },
            {
                "label": "I dont have time",
                "color": "red",
                "function": "showPopup('noTime')"
            },
            {
                "label": "whichNeighbor",
                "color": "red",
                "function": "showPopup('whichNeighbor')"
            },
            {
                "label": "notOwner",
                "color": "red",
                "function": "showPopup('notOwner')"
            },
            {
                "label": "spam",
                "color": "red",
                "function": "showPopup('spamObjection')"
            },
            {
                "label": "howDidYouGetMyNumber",
                "color": "red",
                "function": "showPopup('myNumber')"
            },
            {
                "label": "callBack",
                "color": "red",
                "function": "showPopup('callBack')"
            },
            {
                "label": "nothingIsForFree",
                "color": "red",
                "function": "showPopup('nothingIsForFree')"
            },
            {
                "label": "Next",
                "color": "grey",
                "function": "nextPage",
                "id": "next-btn"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "prevPage",
                "id": "prev-btn"
            },
            {
                "label": "End Call",
                "color": "red",
                "function": "endCallProcess"
            }
        ]
    },
    {
        "page_number": 3,
        "title": "THE INSPECTION PROCESS",
        "content_html": (
            "<span style='font-weight:bold;'>This is How it works:</span><br>"
            "Our inspectors will conduct<br>"
            "a 7-point damage inspection for your property.<br>"
            "They’ll start on the ground level, inspecting:<br>"
            "<ul>"
            "<li>Windows</li>"
            "<li>Screens</li>"
            "<li>Gutters</li>"
            "<li>Downspouts</li>"
            "<li>Garage doors</li>"
            "<li>AC units</li>"
            "<li>Mailbox</li>"
            "</ul>"
            "The reason they start there is<br>"
            "they are looking for signs that<br>"
            "hail has hit the property."
        ),
        "buttons": [
            {
                "label": "sellingMyHome",
                "color": "red",
                "function": "showPopup('sellingMyHome')"
            },
            {
                "label": "noDamage",
                "color": "red",
                "function": "showPopup('noDamage')"
            },
            {
                "label": "Already has a contractor",
                "color": "red",
                "function": "showPopup('hasAContractor')"
            },
            {
                "label": "Next",
                "color": "grey",
                "function": "nextPage",
                "id": "next-btn"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "prevPage",
                "id": "prev-btn"
            },
            {
                "label": "End Call",
                "color": "red",
                "function": "endCallProcess"
            }
        ]
    },
    {
        "page_number": 4,
        "title": "THE INSPECTION PROCESS",
        "content_html": (
            "<span style='font-weight:bold;'>After they complete the ground inspection</span><br>"
            "they will get up on the roof<br>"
            "to do the roof inspection:"
        ),
        "buttons": [
            {
                "label": "alreadyInspected",
                "color": "red",
                "function": "showPopup('alreadyInspected')"
            },
            {
                "label": "noDamage",
                "color": "red",
                "function": "showPopup('noDamage')"
            },
            {
                "label": "Next",
                "color": "grey",
                "function": "nextPage",
                "id": "next-btn"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "prevPage",
                "id": "prev-btn"
            },
            {
                "label": "End Call",
                "color": "red",
                "function": "endCallProcess"
            }
        ]
    },
    {
        "page_number": 5,
        "title": "",
        "content_html": (
            "<span style='color:red; font-weight:bold;'>QUESTION:</span>Now Is your home a 1 or 2-story home<br>"
            "so we bring out the right size ladder?<br><br>"
            "<span style='color:red; font-weight:bold;'>PAUSE AND WAIT FOR A RESPONSE!!!</span><br>"
            "Thank you"
        ),
        "buttons": [
            {
                "label": "Next",
                "color": "grey",
                "function": "nextPage",
                "id": "next-btn"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "prevPage",
                "id": "prev-btn"
            },
            {
                "label": "End Call",
                "color": "red",
                "function": "endCallProcess"
            }
        ]
    },
    {
        "page_number": 6,
        "title": "INSPECTION PROCESS CONTINUED",
        "content_html": (
            "Next, They’ll conduct a roof inspection<br>"
            "by creating a 10-foot by 10-foot<br>"
            "test area on your roof."
        ),
        "buttons": [
            {
                "label": "Next",
                "color": "grey",
                "function": "nextPage",
                "id": "next-btn"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "prevPage",
                "id": "prev-btn"
            },
            {
                "label": "End Call",
                "color": "red",
                "function": "endCallProcess"
            }
        ]
    },
    {
        "page_number": 7,
        "title": "",
        "content_html": (
            "<span style='color:red; font-weight:bold;'>QUESTION:</span> May I ask what type<br>"
            "of roofing do you have on the home?<br>"
            "Is it:<br>"
            "<ul>"
            "<li>Shingle Roofing</li>"
            "<li>Metal Roofing</li>"
            "<li>Tile Roofing</li>"
            "<li>Cedar Shake Roofing</li>"
            "</ul>"
            "<span style='color:red; font-weight:bold;'>PAUSE AND WAIT FOR A RESPONSE!!!</span><br>"
            "Thank You"
        ),
        "buttons": [
            {
                "label": "Next",
                "color": "grey",
                "function": "nextPage",
                "id": "next-btn"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "prevPage",
                "id": "prev-btn"
            },
            {
                "label": "End Call",
                "color": "red",
                "function": "endCallProcess"
            }
        ]
    },
    {
        "page_number": 8,
        "title": "INSPECTION PROCESS CONTINUED",
        "content_html": (
            "Now What They’re Looking For in the Test square<br>"
            "is they are trying to find<br>"
            "6 to 8 hail impacts<br>"
            "to qualify for a full roof replacement.<br>"
            "If they find fewer than that,<br>"
            "it typically means a roof repair is needed."
        ),
        "buttons": [
            {
                "label": "Next",
                "color": "grey",
                "function": "nextPage",
                "id": "next-btn"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "prevPage",
                "id": "prev-btn"
            },
            {
                "label": "End Call",
                "color": "red",
                "function": "endCallProcess"
            }
        ]
    },
    {
        "page_number": 9,
        "title": "CONTINUED INSPECTION QUESTIONS",
        "content_html": (
            "<span style='color:red; font-weight:bold;'>QUESTION:</span> And how old is your<br>"
            "roof on your home? Is it:"
        ),
        "buttons": [
            {
                "label": "1 to 4 years Shingle and Cedar",
                "color": "red",
                "function": "showPopup('1to4ShinglesAndCedar')"
            },
            {
                "label": "5+ Year Shingle and Cedar",
                "color": "green",
                "function": "showPopup('noTimeQualified')"
            },
            {
                "label": "1 year+ Metal & Tile",
                "color": "green",
                "function": "showPopup('noTimeQualified')"
            },
            {
                "label": "1 MONTH TO 11 MONTHS Metal & Tile",
                "color": "red",
                "function": "showPopup('1to4ShinglesAndCedar')"
            },
            {
                "label": "I am Not Interested",
                "color": "red",
                "function": "showPopup('notInterested')"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "prevPage",
                "id": "prev-btn"
            },
            {
                "label": "End Call",
                "color": "red",
                "function": "endCallProcess"
            }
        ]
    },
    {
        "page_number": 10,
        "title": "",
        "content_html": (
            "<span style='color:red; font-weight:bold;'>QUESTION:</span> Alot of your neighbors I have spoken to<br>"
            "Have State Farm and AllState,<br>"
            "Is your Insurance company StateFarm or AllState As Well?<br><br>"
            "<span style='color:red; font-weight:bold;'>PAUSE AND WAIT FOR A RESPONSE!!!</span>"
        ),
        "buttons": [
            {
                "label": "noInsurance",
                "color": "red",
                "function": "showPopup('noInsurance')"
            },
            {
                "label": "nameInsurancNo",
                "color": "green",
                "function": "showPopup('nameInsurancNo')"
            },
            {
                "label": "nameInsuranceYes",
                "color": "green",
                "function": "showPopup('nameInsuranceYes')"
            },
            {
                "label": "myClaimWasDenied",
                "color": "red",
                "function": "showPopup('myClaimWasDenied')"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "prevPage",
                "id": "prev-btn"
            },
            {
                "label": "End Call",
                "color": "red",
                "function": "endCallProcess"
            }
        ]
    },
    {
        "page_number": 11,
        "title": "INSPECTION PROCESS CONTINUED",
        "content_html": (
            "Now If damages are found during the inspection:<br>"
            "<li>They will document the damages.</li>"
            "<li>Take photos.</li><br>"
            "Then, they will sit down with you<br>"
            "and discuss the inspection findings<br>"
            "and explain how they can help you<br>"
            "with the insurance claim process,<br>"
            "ensuring everything is properly paid for<br>"
            "by the insurance company and restored.<br>"
            "<span style='font-weight:bold;'>DOES THAT MAKE SENSE?</span><br>"
            "<span style='color:red; font-weight:bold;'>PAUSE AND WAIT FOR A RESPONSE!!!</span>"
        ),
        "buttons": [
            {
                "label": "insuranceAlreadyCame",
                "color": "red",
                "function": "showPopup('insuranceAlreadyCame')"
            },
            {
                "label": "sellingMyHome",
                "color": "red",
                "function": "showPopup('sellingMyHome')"
            },
            {
                "label": "myClaimWasDenied",
                "color": "red",
                "function": "showPopup('myClaimWasDenied')"
            },
            {
                "label": "alreadyInspected",
                "color": "red",
                "function": "showPopup('alreadyInspected')"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "prevPage",
                "id": "prev-btn"
            },
            {
                "label": "End Call",
                "color": "red",
                "function": "endCallProcess"
            }
        ]
    },
    {
        "page_number": 12,
        "title": "IF THEY FIND NO DAMAGES",
        "content_html": (
            "If they don’t find any damages,<br>"
            "they will share the inspection results<br>"
            "with the National Insurance Restoration Council,<br>"
            "a nonprofit dedicated to helping<br>"
            "property owners in storm-affected areas."
        ),
        "buttons": [
            {
                "label": "whoIsNIRC",
                "color": "red",
                "function": "showPopup('whoIsNIRC')"
            },
            {
                "label": "Next",
                "color": "grey",
                "function": "nextPage",
                "id": "next-btn"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "prevPage",
                "id": "prev-btn"
            },
            {
                "label": "End Call",
                "color": "red",
                "function": "endCallProcess"
            }
        ]
    },
    {
        "page_number": 13,
        "title": "",
        "content_html": (
            "The NIRC will create a certified<br>"
            "No-Damage Inspection Report<br>"
            "and send it to you BY EMAIL for your records.<br><br>"
            "This is a free service to help protect you<br>"
            "from insurance companies denying<br>"
            "your future claims.<br><br>"
            "<span style='font-weight:bold;'>DOES THAT MAKE SENSE?</span><br>"
            "<span style='color:red; font-weight:bold;'>NOW WAIT FOR THEM TO RESPOND</span>"
        ),
        "buttons": [
            {
                "label": "whoIsNIRC",
                "color": "red",
                "function": "showPopup('whoIsNIRC')"
            },
            {
                "label": "Next",
                "color": "grey",
                "function": "nextPage",
                "id": "next-btn"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "prevPage",
                "id": "prev-btn"
            },
            {
                "label": "End Call",
                "color": "red",
                "function": "endCallProcess"
            }
        ]
    },
    {
        "page_number": 14,
        "title": "CONFIRM EMAIL",
        "content_html": (
            "<span style='font-weight:bold;'>RESPONSE:</span> JUST TO CONFIRM,<br>"
            "the email that I have on file<br>"
            "to send the report to<br>"
            "is (Profile.LastName)721@GMAIL.COM<br>"
            "<span style='color:red; font-weight:bold;'>WAIT FOR A RESPONSE SAYING IT IS THE WRONG EMAIL!!</span><br>"
            "<span style='font-weight:bold;'>RESPONSE:</span><br>"
            "Oh goodness, we would have sent the email<br>"
            "to the wrong person.<br>"
            "May I get your correct email?<br>"
            "<span style='color:red; font-weight:bold;'>NOW WAIT FOR THEM TO RESPOND</span>"
        ),
        "buttons": [
            {
                "label": "emailYes",
                "color": "green",
                "function": "showPopup('emailYes')"
            },
            {
                "label": "emailNo",
                "color": "red",
                "function": "showPopup('emailNo')"
            },
            {
                "label": "Why do you need my email?",
                "color": "red",
                "function": "showPopup('myEmail')"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "prevPage",
                "id": "prev-btn"
            },
            {
                "label": "End Call",
                "color": "red",
                "function": "endCallProcess"
            }
        ]
    },
    {
        "page_number": 15,
        "title": "ROOF LEAK AND HOMEOWNER CONFIRMATION",
        "content_html": (
            "<span style='color:red; font-weight:bold;'>QUESTION:</span><br>"
            "Now Have you seen any ROOF leaks,<br>"
            "or water spots; it would look like<br>"
            "coffee stains on the ceiling?<br><br>"
            "<span style='color:red; font-weight:bold;'>NOW WAIT FOR THEM TO RESPOND</span>"
        ),
        "buttons": [
            {
                "label": "yesRoofLeak",
                "color": "green",
                "function": "showPopup('yesRoofLeak')"
            },
            {
                "label": "noRoofLeak",
                "color": "green",
                "function": "showPopup('noRoofLeak')"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "prevPage",
                "id": "prev-btn"
            },
            {
                "label": "End Call",
                "color": "red",
                "function": "endCallProcess"
            }
        ]
    },
    {
        "page_number": 16,
        "title": "CLOSING THE APPOINTMENT",
        "content_html": (
            "<span style='color:red; font-weight:bold;'>QUESTION:</span><br>"
            "I would like to make sure<br>"
            "I have your name correct,<br>"
            "it's (.First Name) (Last Name)?<br><br>"
            "<span style='color:red; font-weight:bold;'>NOW WAIT FOR THEM TO RESPOND</span>"
        ),
        "buttons": [
            {
                "label": "Next",
                "color": "grey",
                "function": "nextPage",
                "id": "next-btn"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "prevPage",
                "id": "prev-btn"
            },
            {
                "label": "End Call",
                "color": "red",
                "function": "endCallProcess"
            }
        ]
    },
    {
        "page_number": 17,
        "title": "CLOSING THE APPOINTMENT",
        "content_html": (
            "<span style='color:red; font-weight:bold;'>QUESTION:</span><br>"
            "Just to verify that I have the<br>"
            "correct address in my records,<br>"
            "I have (FULL ADDRESS)?<br><br>"
            "<span style='color:red; font-weight:bold;'>NOW WAIT FOR THEM TO RESPOND</span><br>"
            "<span style='color:black; font-weight:bold;'>*(If the address is not the same,<br>"
            "verify it and updated in the system) *</span>"
        ),
        "buttons": [
            {
                "label": "Next",
                "color": "grey",
                "function": "nextPage",
                "id": "next-btn"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "prevPage",
                "id": "prev-btn"
            },
            {
                "label": "End Call",
                "color": "red",
                "function": "endCallProcess"
            }
        ]
    },
    {
        "page_number": 18,
        "title": "CLOSING THE APPOINTMENT",
        "content_html": (
            "<span style='color:red; font-weight:bold;'>QUESTION:</span><br>"
            "And you haven’t signed a contract<br>"
            "And you the only homeowner<br>"
            "or decision maker?, correct?<br><br>"
            "<span style='color:red; font-weight:bold;'>NOW WAIT FOR THEM TO RESPOND</span>"
        ),
        "buttons": [
            {
                "label": "notownerlandlord",
                "color": "red",
                "function": "showPopup('notOwnerLandlordObjection')"
            },
            {
                "label": "Yes Owner - Decision Maker",
                "color": "green",
                "function": "nextPage"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "prevPage",
                "id": "prev-btn"
            },
            {
                "label": "End Call",
                "color": "red",
                "function": "endCallProcess"
            }
        ]
    },
    {
        "page_number": 19,
        "title": "CLOSING THE APPOINTMENT",
        "content_html": (
            "<span style='color:red; font-weight:bold;'>QUESTION:</span><br>"
            "And you haven’t signed a contract<br>"
            "with any other roofing company,<br>"
            "correct?<br><br>"
            "<span style='color:red; font-weight:bold;'>NOW WAIT FOR THEM TO RESPOND</span>"
        ),
        "buttons": [
            {
                "label": "nocontractor",
                "color": "green",
                "function": "showPopup('noContractor')"
            },
            {
                "label": "yescontractor",
                "color": "red",
                "function": "showPopup('hasAContractor')"
            },
            {
                "label": "badExperience",
                "color": "red",
                "function": "showPopup('badExperience')"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "prevPage",
                "id": "prev-btn"
            },
            {
                "label": "End Call",
                "color": "red",
                "function": "endCallProcess"
            }
        ]
    },
    {
        "page_number": 20,
        "title": "CLOSING THE APPOINTMENT",
        "content_html": (
            "Just so you know we can work around your schedule,<br>"
            "<span style='color:red; font-weight:bold;'>QUESTION:</span><br>"
            "<span style='color:black; font-weight:bold;'><p>WHAT TIME TOMORROW WORKS BEST FOR YOU</p>"
            "<p>MORNING OR AFTERNOON?</p>:</span><br>"
            "<span style='color:red; font-weight:bold;'>NOW WAIT FOR THEM TO RESPOND</span><br>"
            "<span style='color:black; font-weight:bold;'><p>(Give times available per</p>"
            "<p>calendar link on calendar tab</p>"
            "<p>We can schedule up the three days out</p>"
            "<p>get the day and time confirmed</p>"
        ),
        "buttons": [
            {
                "label": "noTime",
                "color": "red",
                "function": "showPopup('noTime')"
            },
            {
                "label": "cantCallBack",
                "color": "red",
                "function": "showPopup('cantCallYou')"
            },
            {
                "label": "nodecision",
                "color": "red",
                "function": "showPopup('noDecision')"
            },
            {
                "label": "Next",
                "color": "grey",
                "function": "nextPage",
                "id": "next-btn"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "prevPage",
                "id": "prev-btn"
            },
            {
                "label": "End Call",
                "color": "red",
                "function": "endCallProcess"
            }
        ]
    },
    {
        "page_number": 21,
        "title": "FINAL CLOSING AND REFERRALS",
        "content_html": (
            "Well (Profile.First Name),<br>"
            "I want to thank you for your time,<br>"
            "and it was a pleasure speaking with you.<br>"
            "We will see you on<br>"
            "(Appointment date and time) SHARP,<br>"
            "and I CAN COUNT ON YOU BEING THERE THEN?"
        ),
        "buttons": [
            {
                "label": "Next",
                "color": "grey",
                "function": "nextPage",
                "id": "next-btn"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "prevPage",
                "id": "prev-btn"
            },
            {
                "label": "End Call",
                "color": "red",
                "function": "endCallProcess"
            }
        ]
    },
    {
        "page_number": 22,
        "title": "",
        "content_html": (
            "<span style='color:red; font-weight:bold;'>ASK FOR THE SALE DO NOT WIMP OUT</span><br><br>"
            "\"Thank you for setting up<br>"
            "the inspection with us tomorrow.<br><br>"
            "I have just one last favor to ask,<br>"
            "and I hope I have earned<br>"
            "the opportunity.<br>"
            "After we’ve finished<br>"
            "looking at your roof,<br>"
            "I wanted to ask<br>"
            "if there are any neighbors<br>"
            "or friends in the area<br>"
            "that you would not mind<br>"
            "referring me to so we can<br>"
            "provide this service to them as well?<br><br>"
            "If you feel comfortable referring us,<br>"
            "I would greatly appreciate it.<br>"
            "Your support means a lot to me,<br>"
            "and it would really help me<br>"
            "and my family out a lot.\"<br><br>"
            "<span style='color:red; font-weight:bold;'>NOW WAIT FOR THEM TO RESPOND</span>"
        ),
        "buttons": [
            {
                "label": "Yes, Now",
                "color": "green",
                "function": "handleReferralResponse('yes_now')"
            },
            {
                "label": "Yes, Later",
                "color": "yellow",
                "function": "handleReferralResponse('yes_later')"
            },
            {
                "label": "No",
                "color": "red",
                "function": "handleReferralResponse('no')"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "prevPage",
                "id": "prev-btn"
            },
            {
                "label": "End Call",
                "color": "red",
                "function": "endCallProcess"
            }
        ]
    }
}