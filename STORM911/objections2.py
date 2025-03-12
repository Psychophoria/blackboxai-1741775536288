import customtkinter as ctk
from tkinter import messagebox as tkmsg
import re
from config import COLORS, TITLE_FONT

OBJECTION_DEFINITIONS = {
    "myEmail": {
        "title": "Why Do You Need My Email Objection",
        "content_html": (
            "We need your email so I can<br>"
            "<ul>"
            "<p><li>send you the email confirmation of the appointment</li></p>"
            "and <li> so we can email you the<br>"
            "Certified No Damage Inspection<br>"
            "Report for your records.</li>"
            "</ul><br>"
            "We will not and do not use<br>"
            "your email for any other reason at all.<br><br>"
            "Just so you know,<br>"
            "even though we have your email.<br>"
            "Legally I still need to<br>"
            "ask permission to send you an email<br><br>"
            "So may I have permission to send you<br>"
            "<ul>"
            "<li>The Confirmation email.</li>"
            "<li>And the No Damage Inspection Report if needed?</li>"
            "</ul><br>"
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
                "label": "Previous",
                "color": "grey",
                "function": "showPreviousObjectionPopup()"
            },
            {
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "emailYes": {
        "title": "They Gave New Email Address",
        "content_html": (
            "Thank you, Let me update the email<br>"
            "now in our records.<br><br>"
            "<span style='color:red; font-weight:bold;'>Close and Move To Next Question</span>"
        ),
        "buttons": [
            {
                "label": "Previous",
                "color": "grey",
                "function": "showPreviousObjectionPopup()"
            },
            {
                "label": "next",
                "color": "green",
                "function": "nextPage()"
            },
            {
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "emailNo": {
        "title": "Did Not Give A New Email Address",
        "content_html": (
            "Not a problem, we will get it<br>"
            "later if needed.<br><br>"
            "<span style='color:red; font-weight:bold;'>Close and Move To Next Question</span>"
        ),
        "buttons": [
            {
                "label": "Previous",
                "color": "grey",
                "function": "showPreviousObjectionPopup()"
            },
            {
                "label": "next",
                "color": "green",
                "function": "nextPage()"
            },
            {
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "badExperience": {
        "title": "I Had a Bad Experience with Contractors In The Past",
        "content_html": (
            "I completely understand your concern.<br>"
            "Unfortunately, not all contractors<br>"
            "uphold the same standards.<br><br>"
            "That’s exactly why as a NIRC certified contractor<br>"
            "we stand out as an industry leader<br><br>"
            "We’re fully licensed, insured,<br>"
            "and highly rated by homeowners just like you.<br><br>"
            "We prioritize quality work,<br>"
            "clear communication,<br>"
            "and customer satisfaction.<br><br>"
            "Now Let’s get the free Inspection scheduled<br>"
            "so you can experience the difference firsthand!<br><br>"
            "<span style='font-weight:bold;'>DOES THAT SOUND LIKE A GOOD PLAN OF ATTACK?</span><br>"
            "<span style='color:red; font-weight:bold;'>NOW WAIT FOR THEM TO RESPOND</span>"
        ),
        "buttons": [
            {
                "label": "Not Interested",
                "color": "red",
                "function": "showPopup('notInterested')"
            },
            {
                "label": "WantsEstimate",
                "color": "yellow",
                "function": "showPopup('wantsEstimateObjection')"
            },
            {
                "label": "noTime",
                "color": "red",
                "function": "showPopup('noTime')"
            },
            {
                "label": "Failed final try",
                "color": "red",
                "function": "showPopup('failedFinalTryObjection')"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "showPreviousObjectionPopup()"
            },
            {
                "label": "next",
                "color": "green",
                "function": "nextPage()"
            },
            {
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "noInsurance": {
        "title": "Does Not Have insurance Objection",
        "content_html": (
            "Thank you for that information.<br>"
            "However, We require properties<br>"
            "to have homeowners insurance<br>"
            "to set up inspections.<br><br>"
            "Let me check real quick<br>"
            "to see if I have any Contractors<br>"
            "in the Area that are taking<br>"
            "properties with no Insurance"
        ),
        "buttons": [
            {
                "label": "NoInsuranceHaveAContractor",
                "color": "green",
                "function": "showPopup('noInsuranceHaveContractorObjection')"
            },
            {
                "label": "NoInsuranceDontHaveAContractor",
                "color": "red",
                "function": "showPopup('NoInsuranceDontHaveAContractor')"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "showPreviousObjectionPopup()"
            },
            {
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "NoInsuranceDontHaveAContractor": {
        "title": "No Contractor Taking 'No Insurance Appointments'",
        "content_html": (
            "I appreciate your time,<br>"
            "but we won’t be able to<br>"
            "help you at this time<br>"
            "as I dont have any contractors<br>"
            "in the area that are taking properties<br>"
            "with no insurance.<br><br>"
            "<span style='color:red; font-weight:bold;'>END CALL-Call Disposition-No Insurance</span>"
        ),
        "buttons": [
            {
                "label": "Previous",
                "color": "grey",
                "function": "showPreviousObjectionPopup()"
            },
            {
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallAndSetDisposition('No Insurance')"
            }
        ]
    },
    "noInsuranceHaveContractorObjection": {
        "title": "No Insurance, Checking for Contractor",
        "content_html": (
            "\"Thank you for waiting.<br><br>"
            "Unfortunately, at this moment, I do not have a contractor in your area who is able to take appointments for properties without homeowners insurance.<br><br>"
            "In the event that this changes in the future,<br>"
            "would you like us to keep your information on file and reach out if a contractor becomes available?\""
        ),
        "buttons": [
            {
                "label": "Yes, Keep Info",
                "color": "green",
                "function": "handleNoInsuranceKeepInfo('yes')"
            },
            {
                "label": "No, Don't Keep Info",
                "color": "red",
                "function": "triggerEndCallAndSetDisposition('No Insurance')"
            }
        ]
    },
    "noDecision": {
        "title": "noDecision",
        "content_html": (
            "\"I understand your time is valuable,<br>"
            "BUT<br>"
            "Time is running out<br>"
            "to be able to get the damages covered<br>"
            "by your insurance carrier.<br><br>"
            "This will only take a few moments.<br><br>"
            "I am not trying to sell you anything<br>"
            "or have you buy anything,<br>"
            "I am just asking for an opportunity<br>"
            "to earn your business.<br><br>"
            "What I have to go over with you<br>"
            "is important and<br>"
            "I can promise you will see<br>"
            "the value in what I have to say,<br><br>"
            "So,<br>"
            "If I could please have<br>"
            "30 seconds of your time<br>"
            "I will not waist it.<br><br>"
            "PAUSE AND WAIT FOR AN ANSWER.\""
        ),
        "buttons": [
            {
                "label": "Continue",
                "color": "green",
                "function": "nextPage()"
            },
            {
                "label": "Failed final try",
                "color": "red",
                "function": "showPopup('failedFinalTryObjection')"
            },
            {
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "thirtySecondObjection": {
        "title": "thirtySecondObjection",
        "content_html": (
            "\"I understand you don’t<br>"
            "have the time right now,<br>"
            "but<br>"
            "I’m not trying to sell you anything.<br>"
            "I am just asking you for an<br>"
            "opportunity to earn your business.<br>"
            "What I have to go over<br>"
            "with you is important<br>"
            "and it will protect<br>"
            "you in the future.<br><br>"
            "I can promise you will see<br>"
            "the value in what I have to say<br>"
            "so if I could please<br>"
            "have 30 seconds of your time<br>"
            "I promise I will not waist it.<br><br>"
            "PAUSE AND WAIT FOR AN ANSWER!!\""
        ),
        "buttons": [
            {
                "label": "Continue",
                "color": "green",
                "function": "nextPage()"
            },
            {
                "label": "Failed final try",
                "color": "red",
                "function": "showPopup('failedFinalTryObjection')"
            },
            {
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "yesRoofLeak": {
        "title": "yesRoofLeak",
        "content_html": (
            "\"I am glad I asked,<br>"
            "I will make sure to let<br>"
            "the certified contractor know<br>"
            "so they can do an emergency repair<br>"
            "to stop MORE damages from happening.\""
        ),
        "buttons": [
            {
                "label": "close",
                "color": "green",
                "function": "closePopup()"
            }
        ]
    },
    "noRoofLeak": {
        "title": "noRoofLeak",
        "content_html": (
            "\"That’s good news. you are<br>"
            "one of the lucky ones!\""
        ),
        "buttons": [
            {
                "label": "close",
                "color": "green",
                "function": "closePopup()"
            }
        ]
    },
    "notOwnerLandlordObjection": {
        "title": "Not Owner / Landlord Objection",
        "content_html": (
            "\"We need to meet with<br>"
            "the property owner.<br>"
            "Could you provide your<br>"
            "landlord’s contact info<br>"
            "so we can arrange the inspection?<br><br>"
            "PAUSE AND WAIT FOR AN ANSWER!!\""
        ),
        "buttons": [
            {
                "label": "Get Landlord Info",
                "color": "green",
                "function": "handleGetLandlordInfo()"
            },
            {
                "label": "No Landlord Info",
                "color": "red",
                "function": "showPopup('noLandlordInfoObjection')"
            },
            {
                "label": "Not Interested",
                "color": "red",
                "function": "showPopup('notInterested')"
            },
            {
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "noLandlordInfoObjection": {
        "title": "No Landlord Info Objection",
        "content_html": (
            "\"Without the landlord info<br>"
            "we unfortunately cannot proceed.<br><br>"
            "Thank you for your time,<br>"
            "Have a great day.\""
        ),
        "buttons": [
            {
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "hasAContractor": {
        "title": "hasAContractor",
        "content_html": (
            "\"I’m glad you have someone helping.<br>"
            "If you do have any issues<br>"
            "feel free to reach out to us.<br><br>"
            "I thank you for your time<br>"
            "and I hope you have a great day.<br><br>"
            "END CALL CALL<br>"
            "DISPOSITION Not Qualified Contractor.\""
        ),
        "buttons": [
            {
                "label": "End Call",
                "color": "red",
                "function": "triggerEndCallAndSetDisposition('NQ-Has Contractor')"
            }
        ]
    },
    "nameInsuranceYes": {
        "title": "nameInsuranceYes",
        "content_html": (
            "\"Thank you, we have been<br>"
            "dealing a lot with them<br>"
            "and have been very successful<br>"
            "for our clients.\""
        ),
        "buttons": [
            {
                "label": "close",
                "color": "green",
                "function": "closePopup()"
            }
        ]
    },
    "nameInsurancNo": {
        "title": "nameInsurancNo",
        "content_html": (
            "\"No problem; we can get that<br>"
            "information later if you have damages.\""
        ),
        "buttons": [
            {
                "label": "close",
                "color": "green",
                "function": "closePopup()"
            }
        ]
    },
    "noContractor": {
        "title": "noContractor",
        "content_html": (
            "\"That’s fine; we’ll<br>"
            "handle everything for you.\""
        ),
        "buttons": [
            {
                "label": "close",
                "color": "green",
                "function": "closePopup()"
            }
        ]
    },
    "nothingIsForFree": {
        "title": "nothingIsForFree",
        "content_html": (
            "\"Rather than investing heavily<br>"
            "in marketing campaigns,<br>"
            "we prefer to provide you,<br>"
            "our valued customer,<br>"
            "with a free roof inspection.<br><br>"
            "This way, you can<br>"
            "experience our service<br>"
            "first hand and gain a clear,<br>"
            "honest assessment of<br>"
            "your roof’s condition.<br><br>"
            "It's like a free trial<br>"
            "with no obligations<br>"
            "our goal is to build trust<br>"
            "by offering a free property inspection<br>"
            "and seeing how we<br>"
            "can assist you with<br>"
            "any storm restoration needs.<br><br>"
            "<span style='font-weight:bold;'>DOES THAT MAKE SENSE?</span><br>"
            "<span style='color:red; font-weight:bold;'>PAUSE AND WAIT FOR AN ANSWER!!!</span>"
        ),
        "buttons": [
            {
                "label": "Yes, Makes Sense",
                "color": "green",
                "function": "closePopup()"
            },
            {
                "label": "No, Doesn't Make Sense",
                "color": "red",
                "function": "showPopup('doesntMakeSenseObjection')"
            },
            {
                "label": "Not Interested",
                "color": "red",
                "function": "showPopup('notInterested')"
            },
            {
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "myNumber": {
        "title": "myNumber",
        "content_html": (
            "\"We use storm maps to get info<br>"
            "for areas that have been affected<br>"
            "and we use public city records<br>"
            "to access the information.<br><br>"
            "<span style='font-weight:bold;'>DOES THAT MAKE SENSE?</span><br>"
            "<span style='color:red; font-weight:bold;'>PAUSE AND WAIT FOR AN ANSWER!!!</span>\""
        ),
        "buttons": [
            {
                "label": "Yes, Makes Sense",
                "color": "green",
                "function": "closePopup()"
            },
            {
                "label": "No, Doesn't Make Sense",
                "color": "red",
                "function": "showPopup('doesntMakeSenseObjection')"
            },
            {
                "label": "Not Interested",
                "color": "red",
                "function": "showPopup('notInterested')"
            },
            {
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "failed": {
        "title": "failed",
        "content_html": (
            "\"If I may ask you one last question?.<br>"
            "Would you please help me understand<br>"
            "why you are not interested<br>"
            "in the appointment and<br>"
            "how I failed to relay to you<br>"
            "the importance of this call.<br>"
            "So I don’t make<br>"
            "the same mistake with anyone else.<br>"
            "I am trying to help people and<br>"
            "I would really appreciate<br>"
            "knowing how I failed you!<br><br>"
            "<span style='color:red; font-weight:bold;'>PAUSE AND WAIT FOR AN ANSWER!!!</span>\""
        ),
        "buttons": [
            {
                "label": "failResponse",
                "color": "green",
                "function": "showPopup('failResponse')"
            },
            {
                "label": "Not Interested",
                "color": "red",
                "function": "showPopup('notInterested')"
            },
            {
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "spamObjection": {
        "title": "spamObjection",
        "content_html": (
            "\"I understand your concern,<br>"
            "and I'm sorry for any confusion.<br>"
            "Due to the high volume of calls<br>"
            "we make to assist customers<br>"
            "after severe weather,<br>"
            "our number can sometimes<br>"
            "be flagged as spam<br>"
            "by certain systems.<br><br>"
            "We aim to provide<br>"
            "valuable support and services,<br>"
            "and we’re always here to help.<br><br>"
            "<span style='font-weight:bold;'>DOES THAT MAKE SENSE?</span><br>"
            "<span style='color:red; font-weight:bold;'>PAUSE AND WAIT FOR AN ANSWER!!!</span>\""
        ),
        "buttons": [
            {
                "label": "Yes, Makes Sense",
                "color": "green",
                "function": "closePopup()"
            },
            {
                "label": "No, Doesn't Make Sense",
                "color": "red",
                "function": "showPopup('doesntMakeSenseObjection')"
            },
            {
                "label": "Not Interested",
                "color": "red",
                "function": "showPopup('notInterested')"
            },
            {
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "failResponse": {
        "title": "failResponse",
        "content_html": (
            "\"Thank you for that,<br>"
            "so if you would humor me,<br>"
            "I am just asking for an<br>"
            "opportunity to earn your business.<br>"
            "What I must go over with you<br>"
            "is important and I can promise you<br>"
            "will see the value<br>"
            "in what I have to say,<br>"
            "so if I could please have<br>"
            "30 seconds of your time<br>"
            "I will not waist it.<br><br>"
            "<span style='color:red; font-weight:bold;'>PAUSE AND WAIT FOR AN ANSWER!!!</span>\""
        ),
        "buttons": [
            {
                "label": "Continue",
                "color": "green",
                "function": "nextPage()"
            },
            {
                "label": "Not Interested",
                "color": "red",
                "function": "showPopup('notInterested')"
            },
            {
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "dontHaveInfo": {
        "title": "dontHaveInfo",
        "content_html": (
            "\"Can I call you later today<br>"
            "or before the inspection tomorrow morning<br>"
            "so I can reach out to them<br>"
            "that day to get them<br>"
            "all taken care of?<br><br>"
            "<span style='color:red; font-weight:bold;'>PAUSE AND WAIT FOR AN ANSWER!!!</span>\""
        ),
        "buttons": [
            {
                "label": "Yes, Call Back",
                "color": "green",
                "function": "handleCallBackRequest('yes')"
            },
            {
                "label": "No, Don't Call Back",
                "color": "red",
                "function": "triggerEndCallAndSetDisposition('Not Available')"
            },
            {
                "label": "Not Interested",
                "color": "red",
                "function": "showPopup('notInterested')"
            },
            {
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "1to4ShinglesAndCedar": {
        "title": "1to4ShinglesAndCedar",
        "content_html": (
            "\"With the age of your roof,<br>"
            "it is very unlikely that<br>"
            "you have damages as<br>"
            "your roof is very new.<br>"
            "Thank you for your time,<br>"
            "and I hope you have a great day.<br><br>"
            "END THE Call<br>"
            "Call Disposition, Not Qualified Roof Age.\""
        ),
        "buttons": [
            {
                "label": "End Call",
                "color": "red",
                "function": "triggerEndCallAndSetDisposition('NQ-Roof Age')"
            }
        ]
    },
    "referralater": {
        "title": "referralater",
        "content_html": (
            "\"Thank you for the referral,<br>"
            "But<br>"
            "Can I get the info today<br>"
            "so I can reach out to them today<br>"
            "and make sure I can<br>"
            "get it all set up<br>"
            "for the same day.<br>"
            "This way we can inspect<br>"
            "their roof right after yours.<br><br>"
            "<span style='color:red; font-weight:bold;'>PAUSE AND WAIT FOR AN ANSWER!!</span>\""
        ),
        "buttons": [
            {
                "label": "Yes, Give Info Now",
                "color": "green",
                "function": "handleReferralInfoNow('yes')"
            },
            {
                "label": "No, Call Later",
                "color": "yellow",
                "function": "handleReferralInfoNow('no')"
            },
            {
                "label": "Not Interested",
                "color": "red",
                "function": "showPopup('notInterested')"
            },
            {
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "alreadyInspectedYes": {
        "title": "alreadyInspectedYes",
        "content_html": (
            "\"I’m glad to hear that.<br>"
            "Thank you for your time<br>"
            "and have a great day.<br><br>"
            "END CALL<br>"
            "CALL DISPOSITION, Not Qualifiued Has Contractor.\""
        ),
        "buttons": [
            {
                "label": "End Call",
                "color": "red",
                "function": "triggerEndCallAndSetDisposition('NQ-Has Contractor')"
            }
        ]
    },
    "alreadyInspectedNo": {
        "title": "alreadyInspectedNo",
        "content_html": (
            "\"You See, The reason I’m asking is because:<br>"
            "<ul>"
            "<li>You may not have any damages now,<br>"
            "BUT<br>"
            "The next storm may damage your roof.</li>"
            "<li>You see Insurance companies<br>"
            "love to deny roofing claims<br>"
            "by saying everything is old damage.</li>"
            "<li>The No Damage Inspection Report we provide<br>"
            "will protect you against that<br>"
            "as it documents that your roof has<br>"
            "NO storm damages on it now.</li>"
            "<li>Our goal is to protect you for the future.</li>"
            "</ul><br>"
            "This is a free service we provide<br>"
            "as part of giving back<br>"
            "to the areas we provide services in.<br><br>"
            "<span style='font-weight:bold;'>DOES THAT MAKE SENSE?</span><br>"
            "<span style='color:red; font-weight:bold;'>PAUSE AND WAIT FOR AN ANSWER!</span>"
        ),
        "buttons": [
            {
                "label": "Yes, Makes Sense",
                "color": "green",
                "function": "closePopup()"
            },
            {
                "label": "No, Doesn't Make Sense",
                "color": "red",
                "function": "showPopup('doesntMakeSenseObjection')"
            },
            {
                "label": "Not Interested",
                "color": "red",
                "function": "showPopup('notInterested')"
            },
            {
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "wantsEstimateObjection": {
        "title": "Wants Estimate Objection",
        "content_html": (
            "\"We can certainly provide an estimate<br>"
            "if we find damage.<br>"
            "We’ll discuss everything after<br>"
            "the inspection.<br>"
            "Would mornings or afternoons<br>"
            "work best?\""
        ),
        "buttons": [
            {
                "label": "Continue",
                "color": "green",
                "function": "nextPage()"
            },
            {
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "waitingOnInsuranceDecisionObjection": {
        "title": "Waiting On Insurance Decision",
        "content_html": (
            "\"We’d be happy to do a second opinion<br>"
            "inspection in the meantime,<br>"
            "just to confirm no damage is missed.<br>"
            "If everything looks good, great—<br>"
            "If not, we can help ensure your claim is handled properly!\""
        ),
        "buttons": [
            {
                "label": "Continue",
                "color": "green",
                "function": "nextPage()"
            },
            {
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "foundDamagesEstimateObjection": {
        "title": "Found Damages, Has Estimate Objection",
        "content_html": (
            "\"If you already have an estimate,<br>"
            "we can compare and see if anything was missed.<br>"
            "We want to ensure you get<br>"
            "the full coverage you deserve.\""
        ),
        "buttons": [
            {
                "label": "Continue",
                "color": "green",
                "function": "nextPage()"
            },
            {
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "doesntMakeSenseObjection": {
        "title": "Doesn't Make Sense Objection",
        "content_html": (
            "\"Sorry if it’s unclear.<br>"
            "We genuinely aim to offer a free service<br>"
            "to detect storm damage early.<br>"
            "Could you let me know<br>"
            "which part was confusing,<br>"
            "and I’ll clarify?\""
        ),
        "buttons": [
            {
                "label": "Not Interested",
                "color": "red",
                "function": "showPopup('notInterested')"
            },
            {
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    }
}

OBJECTIONS_GROUP_1 = [
    {
        "label": "Thirty Second",
        "id": "thirtySecondObjection",
        "function": "showPopup('thirtySecondObjection')"
    },
    {
        "label": "I don't have time",
        "id": "noTime",
        "function": "showPopup('noTime')"
    },
    {
        "label": "How did I fail you?",
        "id": "failed",
        "function": "showPopup('failed')"
    },
    {
        "label": "I'm not interested",
        "id": "notInterested",
        "function": "showPopup('notInterested')"
    },
    {
        "label": "I already had an inspection",
        "id": "alreadyInspected",
        "function": "showPopup('alreadyInspected')"
    },
    {
        "label": "I don't have any damages",
        "id": "noDamage",
        "function": "showPopup('noDamage')"
    },
    {
        "label": "My Insurance Claim Was Denied",
        "id": "myClaimWasDenied",
        "function": "showPopup('myClaimWasDenied')"
    },
    {
        "label": "I Am Selling My Home",
        "id": "sellingMyHome",
        "function": "showPopup('sellingMyHome')"
    },
    {
        "label": "We have a metal roof",
        "id": "metalRoof",
        "function": "showPopup('metalRoof')"
    },
    {
        "label": "Call Back Later",
        "id": "callBack",
        "function": "showPopup('callBack')"
    },
    {
        "label": "Don't Want To Decide Now",
        "id": "noDecision",
        "function": "showPopup('noDecision')"
    },
    {
        "label": "No Insurance",
        "id": "noInsurance",
        "function": "showPopup('noInsurance')"
    },
    {
        "label": "Not The Homeowner",
        "id": "notOwner",
        "function": "showPopup('notOwner')"
    }
]

OBJECTIONS_GROUP_2 = [
    {
        "label": "Is this a spam call?",
        "id": "spamObjection",
        "function": "showPopup('spamObjection')"
    },
    {
        "label": "How did you get my number?",
        "id": "howDidYouGetMyNumber",
        "function": "showPopup('myNumber')"
    },
    {
        "label": "Who is the NIRC?",
        "id": "whoIsNIRC",
        "function": "showPopup('whoIsNIRC')"
    },
    {
        "label": "Why can't I call you back?",
        "id": "cantCallBack",
        "function": "showPopup('cantCallYou')"
    },
    {
        "label": "I had a bad experience-contractor",
        "id": "hadBadExperience",
        "function": "showPopup('badExperience')"
    },
    {
        "label": "I don’t have homeowners Insurance",
        "id": "noInsurance2",
        "function": "showPopup('noInsurance')"
    },
    {
        "label": "Nothing Is For Free",
        "id": "nothingIsForFree",
        "function": "showPopup('nothingIsForFree')"
    },
    {
        "label": "Which Neighbor are you Inspecting",
        "id": "whichNeighbor",
        "function": "showPopup('whichNeighbor')"
    },
    {
        "label": "Already Has A Contractor",
        "id": "hasAContractor",
        "function": "showPopup('hasAContractor')"
    },
    {
        "label": "Bad Experience",
        "id": "badExperience",
        "function": "showPopup('badExperience')"
    },
    {
        "label": "Thirty Second",
        "id": "thirtySecondObjection2",
        "function": "showPopup('thirtySecondObjection')"
    }
]