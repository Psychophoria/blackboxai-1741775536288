import customtkinter as ctk
from tkinter import messagebox as tkmsg
import re
from config import COLORS, TITLE_FONT

OBJECTION_DEFINITIONS = {
    "noTime": {
        "title": "I Don't Have Time Objection",
        "content_html": (
            "I completely understand that you're busy.<br>"
            "I'm not trying to sell anything; I just want an opportunity<br>"
            "to earn your business.<br><br>"
            "What I’ll cover with you<br>"
            "is quick and valuable,<br>"
            "and it could protect<br>"
            "your home in the future.<br><br>"
            "<span style='color:black; font-weight:bold;'>May I ask the age of your roof?</span><br>"
            "<span style='color:red; font-weight:bold;'>NOW WAIT FOR THEM TO RESPOND</span>"
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
                "label": "notInterestedCloser",
                "color": "red",
                "function": "showPopup('notInterestedCloserObjection')"
            },
            {
                "label": "noDamage",
                "color": "red",
                "function": "showPopup('noDamage')"
            },
            {
                "label": "sellingHouse",
                "color": "red",
                "function": "showPopup('sellingMyHome')"
            },
            {
                "label": "claimDenied",
                "color": "red",
                "function": "showPopup('myClaimWasDenied')"
            },
            {
                "label": "insuranceAlreadyCame",
                "color": "red",
                "function": "showPopup('insuranceAlreadyCame')"
            },
            {
                "label": "hasAContractor",
                "color": "red",
                "function": "showPopup('hasAContractor')"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "showPreviousObjectionPopup()"
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

    "notInterested": {
        "title": "I Am Not Interested Objection",
        "content_html": (
            "I can understand why<br>"
            "you may not be interested right now,<br>"
            "BUT<br><br>"
            "<span style='color:black; font-weight:bold;'>May I ask the age of your roof?</span><br>"
            "<span style='color:red; font-weight:bold;'>NOW WAIT FOR THEM TO RESPOND</span>"
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
                "label": "notInterestedCloser",
                "color": "red",
                "function": "showPopup('notInterestedCloserObjection')"
            },
            {
                "label": "noDamage",
                "color": "red",
                "function": "showPopup('noDamage')"
            },
            {
                "label": "sellingHouse",
                "color": "red",
                "function": "showPopup('sellingMyHome')"
            },
            {
                "label": "claimDenied",
                "color": "red",
                "function": "showPopup('myClaimWasDenied')"
            },
            {
                "label": "insuranceAlreadyCame",
                "color": "red",
                "function": "showPopup('insuranceAlreadyCame')"
            },
            {
                "label": "hasAContractor",
                "color": "red",
                "function": "showPopup('hasAContractor')"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "showPreviousObjectionPopup()"
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

    # -----------------------------------------------
    #   NEWLY ADDED DEFINITION FOR callBack
    # -----------------------------------------------
    "callBack": {
        "title": "Call Back Later",
        "content_html": (
            "I understand you might prefer a call-back.<br>"
            "We can certainly do that.<br><br>"
            "Is there a specific date/time<br>"
            "that would work best for you?"
        ),
        "buttons": [
            {
                "label": "Yes, schedule callback",
                "color": "green",
                "function": "handleCallBackRequest('yes')"
            },
            {
                "label": "No, I'm not interested",
                "color": "red",
                "function": "showPopup('notInterested')"
            },
            {
                "label": "End Call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    # -----------------------------------------------

    "askingOpportunity": {
        "title": "Asking for an Opportunity To Earn Youer Business",
        "content_html": (
            "\"I’m not trying to sell you anything<br>"
            "or have you buy anything.<br>"
            "I’m just asking for an opportunity<br>"
            "to earn your business.<br><br>"
            "What I have to go over with you is important,<br>"
            "and I can promise you,<br>"
            "you will see the value<br>"
            "in what I have to say.<br><br>"
            "So, if I could<br>"
            "please have 30 seconds of your time,<br>"
            "I will not waste it.\""
        ),
        "buttons": [
            {
                "label": "Failed final try",
                "color": "red",
                "function": "showPopup('failedFinalTryObjection')"
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
    "noTimeQualified": {
        "title": "Qualified Roof Age (No Time Issue)",
        "content_html": (
            "\"Great, that means your roof is potentially old enough<br>"
            "that storm damage could be present.<br><br>"
            "Let’s see if we can schedule an inspection...\""
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
    "failedFinalTryObjection": {
        "title": "Failed Final Try Objection",
        "content_html": (
            "It seems we’ve tried multiple times<br>"
            "and you’re still not interested.<br><br>"
            "We’ll have to end the call now,<br>"
            "thanks for your time!"
        ),
        "buttons": [
            {
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "NOT QUALIFIED ROOF AGE": {
        "title": "NOT QUALIFIED ROOF AGE",
        "content_html": (
            "\"With the age of your roof,<br>"
            "it is very unlikely that you have damages<br>"
            "as your roof is very new.<br><br>"
            "<span style='color:black; font-weight:bold;'>END CALL</span><br><br>"
            "CALL DISPOSITION, Not Qualified Roof Age.\""
        ),
        "buttons": [
            {
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallAndSetDisposition('NQ-Roof Age')"
            }
        ]
    },
    "whichNeighbor": {
        "title": "Which Neighbors are you Inspecting",
        "content_html": (
            "We respect our customers privacy,<br>"
            "so we don’t disclose any personal information<br>"
            "without their consent first.<br>"
            "BUT<br>"
            "We will be in the area doing our<br>"
            "appointments helping homeowners<br>"
            "get the support they need<br>"
            "and I would like to get<br>"
            "you on schedule as well.<br><br>"
            "Would Mornings or Afternoons work best for you<br>"
            "so we can a provide you<br>"
            "the free roof inspection<br>"
            "and discuss what we find<br>"
            "and how we can assist you as well?"
        ),
        "buttons": [
            {
                "label": "notInterestedClose",
                "color": "red",
                "function": "showPopup('notInterestedCloserObjection')"
            },
            {
                "label": "Failed final try",
                "color": "red",
                "function": "showPopup('failedFinalTryObjection')"
            },
            {
                "label": "noTime",
                "color": "red",
                "function": "showPopup('noTime')"
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
    "notInterestedCloserObjection": {
        "title": "Not Interested Closer",
        "content_html": (
            "You See, The reason I’m asking is because:<br>"
            "<li>You may not have any damages now,<br>BUT<br>The next storm may damage your roof.</li>"
            "<li>You see Insurance companies<br>"
            "love to deny roofing claims<br>"
            "by saying everything is old damage.</li>"
            "<li>The No Damage Inspection Report we provide<br>"
            "will protect you against that<br>"
            "it documents that your roof has<br>"
            "NO storm damages on it now.</li>"
            "<li>Our goal is to protect you for the future.</li><br>"
            "This is a free service we provide<br>"
            "as part of giving back to the areas<br>"
            "we provide services in.<br>"
            "<span style='font-weight:bold;'>DOES THAT MAKE SENSE?</span><br>"
            "<span style='color:red; font-weight:bold;'>NOW WAIT FOR THEM TO RESPOND</span>"
        ),
        "buttons": [
            {
                "label": "Failed final try",
                "color": "red",
                "function": "showPopup('failedFinalTryObjection')"
            },
            {
                "label": "noTime",
                "color": "red",
                "function": "showPopup('noTime')"
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
    "alreadyInspected": {
        "title": "alreadyInspected",
        "content_html": (
            "When you had it inspected,<br>"
            "did the contractor provide you<br>"
            "with a report stating that the roof<br>"
            "is in good condition<br>"
            "and has no storm damages to it?<br><br>"
            "<span style='color:red; font-weight:bold;'>NOW WAIT FOR THEM TO RESPOND</span>"
        ),
        "buttons": [
            {
                "label": "alreadyInspectedNo",
                "color": "red",
                "function": "showPopup('alreadyInspectedNo')"
            },
            {
                "label": "alreadyInspectedYes",
                "color": "green",
                "function": "showPopup('alreadyInspectedYes')"
            },
            {
                "label": "Not Interested",
                "color": "red",
                "function": "showPopup('notInterested')"
            },
            {
                "label": "insuranceAlreadyCame",
                "color": "red",
                "function": "showPopup('insuranceAlreadyCame')"
            },
            {
                "label": "myClaimWasDenied",
                "color": "red",
                "function": "showPopup('myClaimWasDenied')"
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
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "noDamage": {
        "title": "No Damage Objection",
        "content_html": (
            "You might be right<br>"
            "that your roof doesn’t have any damage,<br>"
            "I’m not trying to sell you anything.<br>"
            "I am just asking you for an opportunity<br>"
            "to earn your business.<br><br>"
            "<span style='color:black; font-weight:bold;'>May I ask the age of your roof?<br>"
            "and what type of roofing do you have</span><br><br>"
            "<span style='color:red; font-weight:bold;'>NOW WAIT FOR THEM TO RESPOND</span>"
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
                "label": "Not Interested",
                "color": "red",
                "function": "showPopup('notInterested')"
            },
            {
                "label": "insuranceAlreadyCame",
                "color": "red",
                "function": "showPopup('insuranceAlreadyCame')"
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
                "label": "metalRoof",
                "color": "red",
                "function": "showPopup('metalRoof')"
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
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "metalRoof": {
        "title": "No Damage Metal Roof Objection",
        "content_html": (
            "I understand, Metal roofs are durable<br>"
            "BUT<br>"
            "can still get damaged in severe storms<br><br>"
            "Our storm inspections can help identify<br>"
            "any issues preventing them<br>"
            "from worsening and ensuring your<br>"
            "roof continues to perform at its best<br><br>"
            "<span style='font-weight:bold;'>DOES THAT MAKE SENSE?</span><br>"
            "<span style='color:red; font-weight:bold;'>NOW WAIT FOR THEM TO RESPOND</span>"
        ),
        "buttons": [
            {
                "label": "Not Interested",
                "color": "red",
                "function": "showPopup('notInterested')"
            },
            {
                "label": "insuranceAlreadyCame",
                "color": "red",
                "function": "showPopup('insuranceAlreadyCame')"
            },
            {
                "label": "myClaimWasDenied",
                "color": "red",
                "function": "showPopup('myClaimWasDenied')"
            },
            {
                "label": "noTime",
                "color": "red",
                "function": "showPopup('noTime')"
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
    "noDamageMetalRoofAge": {
        "title": "No Damage Metal Roof Age",
        "content_html": (
            "May I ask the age of your METAL roof?<br><br>"
            "<span style='color:red; font-weight:bold;'>NOW WAIT FOR THEM TO RESPOND</span>"
        ),
        "buttons": [
            {
                "label": "Yes Makes Sense",
                "color": "red",
                "function": "showPopup('metalRoof')"
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
                "label": "Not Interested",
                "color": "red",
                "function": "showPopup('notInterested')"
            },
            {
                "label": "insuranceAlreadyCame",
                "color": "red",
                "function": "showPopup('insuranceAlreadyCame')"
            },
            {
                "label": "myClaimWasDenied",
                "color": "red",
                "function": "showPopup('myClaimWasDenied')"
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
                "label": "end call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "notOwner": {
        "title": "Did Not Give Property Owners Name",
        "content_html": (
            "I would suggest you contact your landlord<br>"
            "and let them know there may be storm damages<br>"
            "to the roof<br>"
            "so they can get it inspected.<br><br>"
            "I thank you for taking my call<br>"
            "and I hope you have a great day.<br><br>"
            "<span style='color:red; font-weight:bold;'>END THE CALL: Call Disposition-Not Qualified Not Owner</span>"
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
                "function": "triggerEndCallAndSetDisposition('NQ-Not Property Owner')"
            }
        ]
    },
    "theyAreOwner": {
        "title": "They Are The Property Owner",
        "content_html": (
            "Great, Just so you know<br>"
            "we can work around your schedule,<br><br>"
            "WHAT TIME TOMORROW WORKS BEST FOR YOU<br>"
            "MORNING OR AFTERNOON?<br><br>"
            "<span style='color:red; font-weight:bold;'>NOW WAIT FOR THEM TO RESPOND</span><br>"
            "(Give times available per calendar link on calendar tab.<br>"
            "We can schedule up the three days out.)<br>"
            "Get The Day and Time Confirmed"
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
                "label": "End Call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "insuranceAlreadyCame": {
        "title": "Insurance Already Did Inspection Objection",
        "content_html": (
            "That’s great!<br>"
            "Did they find damages to your home?<br><br>"
            "<span style='color:red; font-weight:bold;'>NOW WAIT FOR THEM TO RESPOND</span>"
        ),
        "buttons": [
            {
                "label": "myClaimWasDenied",
                "color": "red",
                "function": "showPopup('myClaimWasDenied')"
            },
            {
                "label": "Waiting On Decision",
                "color": "yellow",
                "function": "showPopup('waitingOnInsuranceDecisionObjection')"
            },
            {
                "label": "Not Interested",
                "color": "red",
                "function": "showPopup('notInterested')"
            },
            {
                "label": "Found Damages-Estimate",
                "color": "green",
                "function": "showPopup('foundDamagesEstimateObjection')"
            },
            {
                "label": "WantsEstimate",
                "color": "yellow",
                "function": "showPopup('wantsEstimateObjection')"
            },
            {
                "label": "Has A Contractor",
                "color": "red",
                "function": "showPopup('hasAContractor')"
            },
            {
                "label": "noTime",
                "color": "red",
                "function": "showPopup('noTime')"
            },
            {
                "label": "Previous",
                "color": "grey",
                "function": "showPreviousObjectionPopup()"
            },
            {
                "label": "End Call",
                "color": "red",
                "function": "triggerEndCallProcess()"
            }
        ]
    },
    "cantCallYou": {
        "title": "Why Can't I Call You Objection",
        "content_html": (
            "Our company prefers to initiate the call,<br>"
            "I use an online dialer since I handle<br>"
            "a high volume of calls each day,<br>"
            "which makes it easier than a standard phone.<br><br>"
            "However, I can easily call you back directly<br>"
            "at a time that works best for you.<br><br>"
            "<span style='font-weight:bold;'>DOES THAT MAKE SENSE?</span><br>"
            "<span style='color:red; font-weight:bold;'>NOW WAIT FOR THEM TO RESPOND</span>"
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
    "sellingMyHome": {
        "title": "Selling My Home Objection",
        "content_html": (
            "Since you're selling your home,<br>"
            "this is actually a great time<br>"
            "to get a storm inspection.<br><br>"
            "We document the roof’s condition,<br>"
            "which can be valuable for potential buyers<br>"
            "and help avoid any surprises<br>"
            "during the appraisal and inspection process.<br><br>"
            "Addressing any storm-related issues now<br>"
            "can also enhance curb appeal,<br>"
            "and if a new roof is needed,<br>"
            "it can increase the property’s value,<br>"
            "making your home even more<br>"
            "attractive to buyers.<br><br>"
            "<span style='font-weight:bold;'>DOES THAT MAKE SENSE?</span><br>"
            "<span style='color:red; font-weight:bold;'>NOW WAIT FOR THEM TO RESPOND</span>"
        ),
        "buttons": [
            {
                "label": "Not Interested",
                "color": "red",
                "function": "showPopup('notInterested')"
            },
            {
                "label": "myClaimWasDenied",
                "color": "red",
                "function": "showPopup('myClaimWasDenied')"
            },
            {
                "label": "noDamage",
                "color": "red",
                "function": "showPopup('noDamage')"
            },
            {
                "label": "metalRoof",
                "color": "red",
                "function": "showPopup('metalRoof')"
            },
            {
                "label": "noTime",
                "color": "red",
                "function": "showPopup('noTime')"
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
    "myClaimWasDenied": {
        "title": "My Claim Was Denied Objection",
        "content_html": (
            "I'm sorry to hear about your experience<br>"
            "with your insurance company.<br>"
            "We specialize in handling<br>"
            "situations like these,<br>"
            "and I can assure you<br>"
            "we are experts in this field<br>"
            "and will make sure<br>"
            "you’re taken care of<br>"
            "every step of the way.<br><br>"
            "If we find damages to the property<br>"
            "we can get it taken care of properly!<br><br>"
            "So,<br>"
            "Would mornings or afternoons<br>"
            "work best for you?<br><br>"
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
    "whoIsNIRC": {
        "title": "Who Is The NIRC Objection",
        "content_html": (
            "The NIRC is a non-profit organization<br>"
            "<ul>"
            "<p><li>with a mission to protect and educate<br>"
            "property owners when dealing with insurance claims.</li></p>"
            "<p><li>They assist property owners<br>"
            "who are having issues dealing<br>"
            "with their insurance companies.</li></p>"
            "<p><li>They have the Best of the Best<br>"
            "Certified Contractor network<br>"
            "who all go through a very tough<br>"
            "background check against the company<br>"
            "and the owners.</li></p>"
            "</ul><br>"
            "<span style='font-weight:bold;'>DOES THAT MAKE SENSE?</span><br>"
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
    }
}