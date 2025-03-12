"""
Main application module for Storm911.
Handles application initialization, GUI setup, and core functionality.
"""

import os
import sys
import logging
import logging.config
import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
from config import (
    COLORS, 
    WINDOW_SIZE, 
    MIN_WINDOW_SIZE, 
    LOGGING_CONFIG, 
    APP_SETTINGS,
    ASSETS_DIR
)

# Configure logging
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

class Storm911App(ctk.CTk):
    """Main application window for Storm911."""
    
    def __init__(self):
        super().__init__()
        
        self.title(APP_SETTINGS["app_name"])
        self.geometry(WINDOW_SIZE)
        self.minsize(*MIN_WINDOW_SIZE)
        
        # Configure appearance
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        # Initialize UI components
        self.setup_ui()
        
        # Initialize event bindings
        self.setup_bindings()
        
        # Load initial data
        self.load_initial_data()
        
        logger.info("Storm911 application initialized")

    def setup_ui(self):
        """Set up the main UI components."""
        # Create main container
        self.main_container = ctk.CTkFrame(self)
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create header
        self.header = ctk.CTkFrame(self.main_container)
        self.header.pack(fill=tk.X, pady=(0, 10))
        
        # App title
        self.title_label = ctk.CTkLabel(
            self.header,
            text=APP_SETTINGS["app_name"],
            font=("Helvetica", 24, "bold")
        )
        self.title_label.pack(side=tk.LEFT, padx=10)
        
        # Navigation buttons
        self.nav_frame = ctk.CTkFrame(self.header)
        self.nav_frame.pack(side=tk.RIGHT, padx=10)
        
        self.home_btn = ctk.CTkButton(
            self.nav_frame,
            text="Home",
            command=self.show_home
        )
        self.home_btn.pack(side=tk.LEFT, padx=5)
        
        self.script_btn = ctk.CTkButton(
            self.nav_frame,
            text="Script",
            command=self.show_script
        )
        self.script_btn.pack(side=tk.LEFT, padx=5)
        
        self.calendar_btn = ctk.CTkButton(
            self.nav_frame,
            text="Calendar",
            command=self.show_calendar
        )
        self.calendar_btn.pack(side=tk.LEFT, padx=5)
        
        # Content area
        self.content_frame = ctk.CTkFrame(self.main_container)
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Status bar
        self.status_bar = ctk.CTkLabel(
            self.main_container,
            text="Ready",
            anchor=tk.W
        )
        self.status_bar.pack(fill=tk.X, pady=(10, 0))

    def setup_bindings(self):
        """Set up event bindings."""
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Add keyboard shortcuts
        self.bind("<Control-q>", lambda e: self.on_closing())
        self.bind("<F1>", lambda e: self.show_help())

    def load_initial_data(self):
        """Load any initial data needed by the application."""
        try:
            # Load saved settings
            self.load_settings()
            
            # Initialize API connection
            self.initialize_api()
            
            # Load user data if available
            self.load_user_data()
            
        except Exception as e:
            logger.error(f"Error loading initial data: {str(e)}")
            messagebox.showerror(
                "Error",
                "Failed to load initial data. Some features may be unavailable."
            )

    def show_home(self):
        """Show the home screen."""
        # Clear current content
        for widget in self.content_frame.winfo_children():
            widget.destroy()
            
        # Add home screen content
        welcome = ctk.CTkLabel(
            self.content_frame,
            text="Welcome to Storm911",
            font=("Helvetica", 20, "bold")
        )
        welcome.pack(pady=20)
        
        self.status_bar.configure(text="Home")

    def show_script(self):
        """Show the call script interface."""
        # Clear current content
        for widget in self.content_frame.winfo_children():
            widget.destroy()
            
        # Add script interface
        from transcript_pages import FULL_SCRIPT_PAGES
        # Initialize script interface here
        
        self.status_bar.configure(text="Call Script")

    def show_calendar(self):
        """Show the calendar interface."""
        # Clear current content
        for widget in self.content_frame.winfo_children():
            widget.destroy()
            
        # Add calendar interface
        # Initialize calendar here
        
        self.status_bar.configure(text="Calendar")

    def show_help(self):
        """Show the help dialog."""
        messagebox.showinfo(
            "Help",
            f"{APP_SETTINGS['app_name']} v{APP_SETTINGS['version']}\n\n"
            f"For support, contact:\n"
            f"Email: {APP_SETTINGS['support_email']}\n"
            f"Phone: {APP_SETTINGS['support_phone']}"
        )

    def load_settings(self):
        """Load application settings."""
        # Load saved settings from file if available
        settings_file = os.path.join(ASSETS_DIR, "settings.json")
        if os.path.exists(settings_file):
            try:
                with open(settings_file, 'r') as f:
                    self.settings = json.load(f)
                logger.info("Settings loaded successfully")
            except Exception as e:
                logger.error(f"Error loading settings: {str(e)}")
                self.settings = {}
        else:
            self.settings = {}

    def initialize_api(self):
        """Initialize API connection."""
        # Initialize API client here
        pass

    def load_user_data(self):
        """Load user data if available."""
        # Load user preferences and data
        pass

    def on_closing(self):
        """Handle application closing."""
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            # Save any necessary data
            try:
                self.save_settings()
            except Exception as e:
                logger.error(f"Error saving settings: {str(e)}")
            
            logger.info("Application closing")
            self.quit()

    def save_settings(self):
        """Save application settings."""
        settings_file = os.path.join(ASSETS_DIR, "settings.json")
        try:
            os.makedirs(ASSETS_DIR, exist_ok=True)
            with open(settings_file, 'w') as f:
                json.dump(self.settings, f)
            logger.info("Settings saved successfully")
        except Exception as e:
            logger.error(f"Error saving settings: {str(e)}")
            raise

def run_app():
    """Run the Storm911 application."""
    try:
        app = Storm911App()
        app.mainloop()
    except Exception as e:
        logger.critical(f"Application failed to start: {str(e)}")
        messagebox.showerror(
            "Error",
            "Failed to start the application. Please check the logs for details."
        )
        sys.exit(1)

if __name__ == "__main__":
    run_app()

        # Build the GUI
        self.create_header()
        self.create_main_content()

    # ---------------------------------------------------------------------
    # HEADER
    # ---------------------------------------------------------------------
    def create_header(self):
        header_frame = ctk.CTkFrame(self, height=60)
        header_frame.pack(fill="x", padx=10, pady=10)

        try:
            # Left image
            assure_path = os.path.join(ASSETS_DIR, "assurecall.png")
            assure_img = Image.open(assure_path)
            assure_ph = ImageTk.PhotoImage(assure_img)
            left_lbl = ctk.CTkLabel(header_frame, image=assure_ph, text="")
            left_lbl.image = assure_ph
            left_lbl.pack(side="left", padx=10)

            # Center (top) image
            storm_path = os.path.join(ASSETS_DIR, "storm911.png")
            storm_img = Image.open(storm_path)
            storm_ph = ImageTk.PhotoImage(storm_img)
            center_lbl = ctk.CTkLabel(header_frame, image=storm_ph, text="")
            center_lbl.image = storm_ph
            center_lbl.pack(side="top", pady=5)

        except Exception as e:
            logger.error(f"Header image error: {e}")

    # ---------------------------------------------------------------------
    # MAIN CONTENT
    # ---------------------------------------------------------------------
    def create_main_content(self):
        content = ctk.CTkFrame(self)
        content.pack(expand=True, fill="both", padx=10, pady=(0,10))
        content.grid_columnconfigure(0, weight=2)
        content.grid_columnconfigure(1, weight=4)
        content.grid_columnconfigure(2, weight=4)

        # LEFT
        self.left_panel = ctk.CTkFrame(content, fg_color=COLORS["white"])
        self.left_panel.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.build_caller_data_panel()

        # CENTER
        self.center_panel = ctk.CTkFrame(content, fg_color=COLORS["white"])
        self.center_panel.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.build_transcript_panel()

        # RIGHT
        self.right_panel = ctk.CTkFrame(content, fg_color=COLORS["white"])
        self.right_panel.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)
        self.build_objections_panel()

    # ---------------------------------------------------------------------
    # LEFT PANEL - CALLER DATA
    # ---------------------------------------------------------------------
    def build_caller_data_panel(self):
        title = ctk.CTkLabel(
            self.left_panel,
            text="CALLER DATA & INFO",
            font=HEADER_FONT,
            text_color=COLORS["primary_blue"]
        )
        title.pack(pady=5)

        search_frame = ctk.CTkFrame(self.left_panel, fg_color=COLORS["light_grey"])
        search_frame.pack(fill="x", padx=5, pady=5)

        ctk.CTkLabel(search_frame, text="Phone:", font=DEFAULT_FONT).pack(side="left", padx=5)
        phone_ent = ctk.CTkEntry(search_frame, textvariable=self.phone_search_var, width=120)
        phone_ent.pack(side="left", padx=5)
        btn = ctk.CTkButton(search_frame, text="SEARCH / LOAD", command=self.handle_lead_search)
        btn.pack(side="left", padx=5)

        data_frame = ctk.CTkFrame(self.left_panel, fg_color=COLORS["white"])
        data_frame.pack(expand=True, fill="both", padx=5, pady=5)

        ctk.CTkLabel(
            data_frame,
            text="Customer Information",
            font=TITLE_FONT,
            text_color=COLORS["primary_blue"]
        ).pack(anchor="w", pady=(5,2))

        self.add_field(data_frame, "Customer's Name:", self.customer_name_var)
        self.add_field(data_frame, "Address:", self.address_var)
        self.add_field(data_frame, "City:", self.city_var)
        self.add_field(data_frame, "State:", self.state_var)
        self.add_field(data_frame, "Zip Code:", self.zip_var)
        self.add_field(data_frame, "Phone Number:", self.phone_var)
        self.add_field(data_frame, "Cell Number:", self.cell_var)
        self.add_field(data_frame, "Email:", self.email_var)

        ctk.CTkLabel(
            data_frame,
            text="Roofing Information",
            font=TITLE_FONT,
            text_color=COLORS["primary_blue"]
        ).pack(anchor="w", pady=(15,2))

        self.add_dropdown(data_frame, "How Many Stories:", self.roof_stories_var,
                          ["Select Roof Stories","1 Story","1.5 Stories","2 Stories"])
        self.add_dropdown(data_frame, "Roof Age:", self.roof_age_var,
                          ["Select Roof Age","1-4 Years","5-9 Years","10+ Years"])
        self.add_dropdown(data_frame, "Roofing Type:", self.roof_type_var,
                          ["Select Roofing Type","Shingles","Metal","Tile","Cedar Shake"])

        ctk.CTkLabel(
            data_frame,
            text="Insurance & Appointment",
            font=TITLE_FONT,
            text_color=COLORS["primary_blue"]
        ).pack(anchor="w", pady=(15,2))

        self.add_dropdown(
            data_frame,
            "Do You Have Homeowners Insurance?",
            self.has_insurance_var,
            ["Select Response","Yes","No"],
            command=self.on_ins_change
        )

        ins_comp_frame = ctk.CTkFrame(data_frame)
        ins_comp_frame.pack(fill="x", pady=2)
        ins_comp_lbl = ctk.CTkLabel(ins_comp_frame, text="Insurance Company Name:", font=DEFAULT_FONT)
        ins_comp_lbl.pack(side="left", padx=5)
        self.insurance_entry = ctk.CTkEntry(
            ins_comp_frame,
            textvariable=self.insurance_company_var,
            state="disabled"
        )
        self.insurance_entry.pack(side="left", padx=5, fill="x", expand=True)

        self.add_dropdown(
            data_frame,
            "Are you the homeowner / decision maker?",
            self.is_homeowner_var,
            ["Select Response","Yes","No"]
        )
        self.add_dropdown(
            data_frame,
            "You Don't Have A Contractor Currently?",
            self.has_contractor_var,
            ["Select response","Yes","No"]
        )

        self.add_field(data_frame, "Appointment Date (mm/dd/yyyy):", self.appointment_date_var)
        self.add_dropdown(
            data_frame,
            "Appointment Time:",
            self.appointment_time_var,
            ["Select Appointment Time","9:00 AM","10:00 AM","11:00 AM","12:00 PM",
             "1:00 PM","2:00 PM","3:00 PM","4:00 PM","5:00 PM","6:00 PM","7:00 PM"]
        )

    def add_field(self, parent, label_text, var):
        frame = ctk.CTkFrame(parent)
        frame.pack(fill="x", pady=2)
        lbl = ctk.CTkLabel(frame, text=label_text, font=DEFAULT_FONT)
        lbl.pack(side="left", padx=5)
        ent = ctk.CTkEntry(frame, textvariable=var, width=160)
        ent.pack(side="left", padx=5, fill="x", expand=True)
        return ent

    def add_dropdown(self, parent, label_text, var, values, command=None):
        frame = ctk.CTkFrame(parent)
        frame.pack(fill="x", pady=2)
        lbl = ctk.CTkLabel(frame, text=label_text, font=DEFAULT_FONT)
        lbl.pack(side="left", padx=5)
        dd = ctk.CTkOptionMenu(frame, variable=var, values=values, command=command)
        dd.pack(side="left", padx=5)
        return dd

    def on_ins_change(self, choice):
        if choice == "Yes":
            self.insurance_entry.configure(state="normal")
        else:
            self.insurance_company_var.set("")
            self.insurance_entry.configure(state="disabled")

    def handle_lead_search(self):
        phone = self.phone_search_var.get().strip()
        if not phone:
            tkmsg.showwarning("Error", "Enter phone number to search.")
            return

        url = f"{READYMODE_API_BASE}/search/Lead/{phone}"
        params = {
            "API_user": self.credentials["username"],
            "API_pass": self.credentials["password"]
        }
        try:
            r = requests.get(url, params=params)
            if r.status_code == 200:
                data = r.json()
                if data.get("status") == "success":
                    ans = tkmsg.askyesno("Lead Found", "Populate data from lead?")
                    if ans:
                        self.populate_lead_data(data)
                else:
                    tkmsg.showinfo("No Lead", "No lead found.")
            else:
                tkmsg.showwarning("Error", "Error searching lead. Invalid credentials or phone?")
        except Exception as e:
            logger.error(f"Search error: {e}")
            tkmsg.showwarning("Error", "Connection error searching lead.")

    def populate_lead_data(self, lead_json):
        lead = lead_json.get("lead", {})
        self.customer_name_var.set(lead.get("firstName","John")+" "+lead.get("lastName","Doe"))
        self.address_var.set(lead.get("address","123 Example St"))
        self.city_var.set(lead.get("city","SampleCity"))
        self.state_var.set(lead.get("state","TX"))
        self.zip_var.set(lead.get("zip","99999"))
        self.phone_var.set(lead.get("phone","0000000000"))
        self.cell_var.set("")
        self.email_var.set(lead.get("email","test@example.com"))
        self.roof_stories_var.set("1 Story")
        self.roof_age_var.set("5-9 Years")
        self.roof_type_var.set("Shingles")
        self.has_insurance_var.set("Yes")
        self.insurance_company_var.set("Allstate")
        self.is_homeowner_var.set("Yes")
        self.has_contractor_var.set("No")
        self.appointment_date_var.set("01/01/2025")
        self.appointment_time_var.set("10:00 AM")

    # ---------------------------------------------------------------------
    # CENTER PANEL - SCRIPT / TRANSCRIPT
    # ---------------------------------------------------------------------
    def build_transcript_panel(self):
        lbl = ctk.CTkLabel(
            self.center_panel,
            text="TRANSCRIPT",
            font=HEADER_FONT,
            text_color=COLORS["primary_blue"]
        )
        lbl.pack(pady=5)

        self.script_box = ctk.CTkTextbox(self.center_panel, wrap="word", width=400, height=400)
        self.script_box.pack(expand=True, fill="both", padx=5, pady=5)

        nav_frame = ctk.CTkFrame(self.center_panel)
        nav_frame.pack(fill="x", padx=5, pady=5)

        self.prev_btn = ctk.CTkButton(nav_frame, text="Previous", command=self.go_previous)
        self.prev_btn.pack(side="left", padx=5)

        self.next_btn = ctk.CTkButton(nav_frame, text="Next", command=self.go_next)
        self.next_btn.pack(side="left", padx=5)

        self.end_call_btn = ctk.CTkButton(
            nav_frame,
            text="END CALL",
            fg_color=COLORS["error_red"],
            command=self.confirm_end_call
        )
        self.end_call_btn.pack(side="left", padx=5)

        self.reset_btn = ctk.CTkButton(
            nav_frame,
            text="RESET",
            fg_color=COLORS["neutral_grey"],
            command=self.confirm_reset
        )
        self.reset_btn.pack(side="left", padx=5)

        self.display_script_page(0)

    def display_script_page(self, idx):
        self.current_page_index = idx
        page = FULL_SCRIPT_PAGES[idx]

        self.script_box.delete("1.0", "end")

        if page["title"]:
            self.script_box.insert("end", page["title"] + "\n\n")

        content_txt = page["content_html"].replace("<br>", "\n").replace("<li>", " - ").replace("</li>", "\n")
        content_txt = re.sub(r"<[^>]+>", "", content_txt)
        self.script_box.insert("end", content_txt)

        if idx == 0:
            self.prev_btn.configure(state="disabled")
            self.next_btn.configure(state="disabled")
            self.end_call_btn.configure(state="disabled")
            self.reset_btn.configure(state="disabled")
        else:
            self.prev_btn.configure(state="normal" if idx > 1 else ("disabled" if idx == 1 else "normal"))
            if idx == self.total_pages - 1:
                self.next_btn.configure(state="disabled")
            else:
                self.next_btn.configure(state="normal")
            self.end_call_btn.configure(state="normal")
            self.reset_btn.configure(state="normal")

    def go_previous(self):
        if self.current_page_index > 0:
            self.display_script_page(self.current_page_index - 1)

    def go_next(self):
        if self.current_page_index < (self.total_pages - 1):
            self.display_script_page(self.current_page_index + 1)

    def confirm_end_call(self):
        """Confirm end call and open disposition window."""
        ans = tkmsg.askyesno("Confirm End Call", "Are you sure you want to END CALL?")
        if ans:
            # Check if we have appointment details already
            has_appointment = (
                self.appointment_date_var.get().strip() != "" and 
                self.appointment_time_var.get() != "Select Appointment Time"
            )
            # Open call disposition with appointment scheduling
            CallDispositionPopup(self, self, show_appointment=not has_appointment)

    def reset_all(self):
        """Reset all form fields and variables to their default state."""
        self.phone_search_var.set("")
        self.customer_name_var.set("")
        self.address_var.set("")
        self.city_var.set("")
        self.state_var.set("")

    # ---------------------------------------------------------------------
    # RIGHT PANEL - OBJECTIONS
    # ---------------------------------------------------------------------
    def build_objections_panel(self):
        lbl = ctk.CTkLabel(
            self.right_panel,
            text="OBJECTIONS",
            font=HEADER_FONT,
            text_color=COLORS["primary_blue"]
        )
        lbl.pack(pady=5)

        obj_panel = ctk.CTkFrame(self.right_panel, fg_color=COLORS["white"])
        obj_panel.pack(expand=True, fill="both", padx=5, pady=5)

        col1 = ctk.CTkFrame(obj_panel, fg_color=COLORS["white"])
        col2 = ctk.CTkFrame(obj_panel, fg_color=COLORS["white"])
        col1.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        col2.pack(side="left", expand=True, fill="both", padx=5, pady=5)

        for item in OBJECTIONS_GROUP_1:
            b = ctk.CTkButton(
                col1,
                text=item["label"],
                fg_color=COLORS["primary_blue"],
                command=lambda i=item: self.show_objection(i)
            )
            b.pack(fill="x", padx=5, pady=5)

        for item in OBJECTIONS_GROUP_2:
            b = ctk.CTkButton(
                col2,
                text=item["label"],
                fg_color=COLORS["primary_blue"],
                command=lambda i=item: self.show_objection(i)
            )
            b.pack(fill="x", padx=5, pady=5)

    def show_objection(self, item):
        oid = item["id"]
        if oid in OBJECTION_DEFINITIONS:
            ObjectionPopup(self, oid, self)
        else:
            tkmsg.showwarning("Error", f"No definition for {oid}")

    def collectDataForPDF(self):
        data_map = {
            "Lead.campaign": "Storm911",
            "Profile.First Name": self.customer_name_var.get().split(" ")[0]
                                 if self.customer_name_var.get() else "",
            "Profile.Last Name": " ".join(self.customer_name_var.get().split(" ")[1:])
                                 if len(self.customer_name_var.get().split(" ")) > 1 else "",
            "Profile.Address": self.address_var.get(),
            "Profile.City": self.city_var.get(),
            "Profile.State": self.state_var.get(),
            "Profile.Zip Code": self.zip_var.get(),
            "Profile.Phone Number": self.phone_var.get(),
            "Profile.Cell Phone": self.cell_var.get(),
            "Profile.Has Insurance": self.has_insurance_var.get(),
            "Profile. Insurance Co. Name": self.insurance_company_var.get(),
            "Profile.Email": self.email_var.get(),
            "Profile.Roof Type": self.roof_type_var.get(),
            "Profile.Roof Age": self.roof_age_var.get(),
            "Profile.How Many Stories is House": self.roof_stories_var.get(),
            "Profile.Call Notes": "",
            "Profile.Appointment Time.Date": self.appointment_date_var.get(),
            "Profile.Appointment Time.Time": self.appointment_time_var.get(),
            "Profile.Appointment Confirmed": "Yes"
        }
        return data_map


# -------------------------------------------------------------------------
# CALL DISPOSITION POPUP (CTkToplevel)
# -------------------------------------------------------------------------
class CallDispositionPopup(ctk.CTkToplevel):
    def __init__(self, master, main_gui, show_appointment: bool = False):
        super().__init__(master)
        self.main_gui = main_gui
        self.show_appointment = show_appointment
        self.title("CALL DISPOSITION")
        self.geometry("800x600")
        self.configure(fg_color=COLORS["light_grey"])
        self.grab_set()
        
        # Create two columns
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Left column - Disposition
        left_frame = ctk.CTkFrame(self)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        disp_label = ctk.CTkLabel(
            left_frame,
            text="Select Call Disposition:",
            font=TITLE_FONT,
            text_color=COLORS["primary_blue"]
        )
        disp_label.pack(pady=5)

        self.disp_var = ctk.StringVar(value="Select Disposition")
        self.dropdown = ctk.CTkOptionMenu(
            left_frame,
            variable=self.disp_var,
            values=["Select Disposition","Not Interested","Qualified - Appt Set",
                    "NQ-Roof Age","NQ-Has Contractor","No Insurance"],
            command=self.on_disposition_change
        )
        self.dropdown.pack(pady=5)
        
        # Right column - Appointment (if enabled)
        if show_appointment:
            right_frame = ctk.CTkFrame(self)
            right_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
            
            appt_label = ctk.CTkLabel(
                right_frame,
                text="Schedule Appointment:",
                font=TITLE_FONT,
                text_color=COLORS["primary_blue"]
            )
            appt_label.pack(pady=5)
            
            self.schedule_btn = ctk.CTkButton(
                right_frame,
                text="Open Scheduler",
                command=self.open_scheduler,
                state="disabled"
            )
            self.schedule_btn.pack(pady=5)

        # Bottom buttons frame
        btn_frame = ctk.CTkFrame(self)
        btn_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        
        submit_btn = ctk.CTkButton(
            btn_frame,
            text="SUBMIT",
            fg_color=COLORS["success_green"],
            command=self.submit_disposition
        )
        submit_btn.pack(side="left", padx=5)

        act_label = ctk.CTkLabel(
            self,
            text="Post-Call Actions:",
            font=TITLE_FONT,
            text_color=COLORS["primary_blue"]
        )
        act_label.pack(pady=5)

        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(pady=5)

        export_pdf_btn = ctk.CTkButton(
            btn_frame,
            text="EXPORT PDF",
            fg_color=COLORS["primary_blue"],
            command=self.open_pdf_export
        )
        export_pdf_btn.pack(side="left", padx=5)

        send_email_btn = ctk.CTkButton(
            btn_frame,
            text="SEND EMAIL",
            fg_color=COLORS["warning_yellow"],
            command=self.open_email_send
        )
        send_email_btn.pack(side="left", padx=5)

        cancel_btn = ctk.CTkButton(
            btn_frame,
            text="CANCEL",
            fg_color=COLORS["error_red"],
            command=self.cancel_disposition
        )
        cancel_btn.pack(side="left", padx=10, pady=10)

        reset_btn = ctk.CTkButton(
            btn_frame,
            text="RESET",
            fg_color=COLORS["neutral_grey"],
            command=self.reset_call
        )
        reset_btn.pack(side="right", padx=10, pady=10)

    def on_disposition_change(self, value: str):
        """Enable/disable appointment scheduling based on disposition."""
        if self.show_appointment:
            if value == "Qualified - Appt Set":
                self.schedule_btn.configure(state="normal")
            else:
                self.schedule_btn.configure(state="disabled")
    
    def open_scheduler(self):
        """Open appointment scheduler window."""
        AppointmentWindow(self, callback=self.on_appointment_set)
    
    def on_appointment_set(self, appointment: Dict):
        """Handle appointment being set."""
        logger.info(f"Appointment set: {appointment}")
        tkmsg.showinfo("Success", "Appointment scheduled successfully!")
    
    def submit_disposition(self):
        """Submit call disposition and handle appointment if set."""
        disp = self.disp_var.get()
        logger.info(f"Call Disposition selected: {disp}")
        
        if disp == "Qualified - Appt Set" and self.show_appointment:
            if not hasattr(self, 'appointment_set'):
                ans = tkmsg.askyesno(
                    "Schedule Appointment",
                    "Would you like to schedule the appointment now?"
                )
                if ans:
                    self.open_scheduler()
                    return
                    
        tkmsg.showinfo("Disposition", f"Disposition set to: {disp}")

    def open_pdf_export(self):
        PDFExportPopup(self, self.main_gui)

    def open_email_send(self):
        EmailSendPopup(self, self.main_gui)

    def cancel_disposition(self):
        ans = tkmsg.askyesno("Cancel", "Are you sure you want to CANCEL?")
        if ans:
            self.destroy()

    def reset_call(self):
        ans = tkmsg.askyesno("Confirm Reset", "Are you sure you want to RESET?")
        if ans:
            self.destroy()
            self.main_gui.reset_all()


# -------------------------------------------------------------------------
# PDF EXPORT POPUP (CTkToplevel)
# -------------------------------------------------------------------------
class PDFExportPopup(ctk.CTkToplevel):
    def __init__(self, master, main_gui):
        super().__init__(master)
        self.master_popup = master
        self.main_gui = main_gui
        self.title("Export PDF")
        self.geometry("700x500")
        self.configure(fg_color=COLORS["light_grey"])
        self.grab_set()

        lbl = ctk.CTkLabel(
            self,
            text="Select PDF Template:",
            font=TITLE_FONT,
            text_color=COLORS["primary_blue"]
        )
        lbl.pack(pady=5)

        self.template_var = ctk.StringVar(value=PDF_EMAIL_TEMPLATES[0]["name"])
        template_names = [t["name"] for t in PDF_EMAIL_TEMPLATES]
        self.dropdown = ctk.CTkOptionMenu(
            self,
            variable=self.template_var,
            values=template_names,
            command=self.update_preview
        )
        self.dropdown.pack(pady=5)

        self.preview_box = ctk.CTkTextbox(self, wrap="word", width=600, height=300)
        self.preview_box.pack(expand=True, fill="both", padx=10, pady=10)

        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(pady=10)

        export_btn = ctk.CTkButton(
            btn_frame,
            text="EXPORT",
            fg_color=COLORS["success_green"],
            command=self.export_pdf
        )
        export_btn.pack(side="left", padx=5)

        close_btn = ctk.CTkButton(
            btn_frame,
            text="BACK",
            fg_color=COLORS["neutral_grey"],
            command=self.destroy
        )
        close_btn.pack(side="left", padx=5)

        self.update_preview(self.template_var.get())

    def update_preview(self, choice):
        for t in PDF_EMAIL_TEMPLATES:
            if t["name"] == choice:
                self.preview_box.delete("1.0", "end")
                self.preview_box.insert("1.0", t["content"])
                break

    def export_pdf(self):
        data_map = self.main_gui.collectDataForPDF()
        chosen_name = self.template_var.get()
        template_content = ""
        for tpl in PDF_EMAIL_TEMPLATES:
            if tpl["name"] == chosen_name:
                template_content = tpl["content"]
                break

        replaced_text = self.replace_placeholders(template_content, data_map)
        filename = chosen_name.replace(" ", "_") + ".pdf"
        filepath = os.path.join(EXPORTS_DIR, filename)

        doc = SimpleDocTemplate(filepath, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []
        for line in replaced_text.split("\n"):
            story.append(Paragraph(line, styles["Normal"]))
            story.append(Spacer(1, 12))
        doc.build(story)

        tkmsg.showinfo("PDF Export", f"PDF exported to {filepath}")
        self.destroy()

    def replace_placeholders(self, text, data_map):
        for k, v in data_map.items():
            text = text.replace(f"({k})", sanitize_input(v))
        return text


# -------------------------------------------------------------------------
# EMAIL SEND POPUP (CTkToplevel)
# -------------------------------------------------------------------------
class EmailSendPopup(ctk.CTkToplevel):
    def __init__(self, master, main_gui):
        super().__init__(master)
        self.master_popup = master
        self.main_gui = main_gui
        self.title("Send Email")
        self.geometry("700x500")
        self.configure(fg_color=COLORS["light_grey"])
        self.grab_set()

        lbl = ctk.CTkLabel(
            self,
            text="Select Email Template:",
            font=TITLE_FONT,
            text_color=COLORS["primary_blue"]
        )
        lbl.pack(pady=5)

        self.template_var = ctk.StringVar(value=PDF_EMAIL_TEMPLATES[0]["name"])
        template_names = [t["name"] for t in PDF_EMAIL_TEMPLATES]
        self.dropdown = ctk.CTkOptionMenu(
            self,
            variable=self.template_var,
            values=template_names,
            command=self.update_preview
        )
        self.dropdown.pack(pady=5)

        subj_label = ctk.CTkLabel(self, text="Email Subject:")
        subj_label.pack()
        self.subject_var = ctk.StringVar(value="Storm911 Report")
        self.subj_entry = ctk.CTkEntry(self, textvariable=self.subject_var, width=600)
        self.subj_entry.pack(padx=10, pady=5)

        self.body_box = ctk.CTkTextbox(self, wrap="word", width=600, height=300)
        self.body_box.pack(expand=True, fill="both", padx=10, pady=10)

        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(pady=10)

        send_btn = ctk.CTkButton(
            btn_frame,
            text="SEND",
            fg_color=COLORS["success_green"],
            command=self.send_email
        )
        send_btn.pack(side="left", padx=5)

        close_btn = ctk.CTkButton(
            btn_frame,
            text="BACK",
            fg_color=COLORS["neutral_grey"],
            command=self.destroy
        )
        close_btn.pack(side="left", padx=5)

        self.update_preview(self.template_var.get())

    def update_preview(self, choice):
        data_map = self.main_gui.collectDataForPDF()
        template_content = ""
        for tpl in PDF_EMAIL_TEMPLATES:
            if tpl["name"] == choice:
                template_content = tpl["content"]
                break
        replaced = self.replace_placeholders(template_content, data_map)

        self.body_box.delete("1.0","end")
        self.body_box.insert("1.0", replaced)

    def send_email(self):
        subject = self.subject_var.get().strip()
        body = self.body_box.get("1.0","end").strip()
        if not subject or not body:
            tkmsg.showwarning("Error", "Subject or body is empty.")
            return
        recipient = SMTP_SETTINGS["default_recipient"]
        try:
            msg = MIMEMultipart()
            msg["From"] = SMTP_SETTINGS["username"]
            msg["To"] = recipient
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            server = smtplib.SMTP(SMTP_SETTINGS["server"], SMTP_SETTINGS["port"])
            server.starttls()
            server.login(SMTP_SETTINGS["username"], SMTP_SETTINGS["password"])
            server.send_message(msg)
            server.quit()

            tkmsg.showinfo("Email Sent", f"Email sent to {recipient}")
            self.destroy()
        except Exception as e:
            logger.error(f"Email send error: {e}")
            tkmsg.showwarning("Error", "Failed to send email.")

    def replace_placeholders(self, text, data_map):
        for k, v in data_map.items():
            text = text.replace(f"({k})", sanitize_input(v))
        return text


# -------------------------------------------------------------------------
# OBJECTION POPUP (CTkToplevel)
# -------------------------------------------------------------------------
class ObjectionPopup(ctk.CTkToplevel):
    def __init__(self, master, objection_id, main_gui):
        super().__init__(master)
        self.main_gui = main_gui
        self.objection_id = objection_id
        self.title(objection_id)
        self.configure(fg_color=COLORS["light_grey"])
        self.grab_set()

        w, h = 600, 400
        parent_x = master.winfo_rootx()
        parent_y = master.winfo_rooty()
        parent_w = master.winfo_width()
        parent_h = master.winfo_height()
        xpos = parent_x + (parent_w // 2) - (w // 2)
        ypos = parent_y + (parent_h // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{xpos}+{ypos}")

        obj_def = OBJECTION_DEFINITIONS.get(objection_id, None)
        if obj_def:
            t = ctk.CTkLabel(
                self,
                text=obj_def["title"],
                font=TITLE_FONT,
                text_color=COLORS["primary_blue"]
            )
            t.pack(pady=5)

            tb = ctk.CTkTextbox(self, wrap="word")
            tb.pack(expand=True, fill="both", padx=10, pady=10)

            content_txt = obj_def["content_html"].replace("<br>", "\n").replace("<li>", " - ").replace("</li>", "\n")
            content_txt = re.sub(r"<[^>]+>", "", content_txt)
            tb.insert("1.0", content_txt)
            tb.configure(state="disabled")

            btn_frame = ctk.CTkFrame(self)
            btn_frame.pack(pady=5)

            for bdef in obj_def["buttons"]:
                color_code = COLORS.get(bdef.get("color","neutral_grey"), "#777777")
                b = ctk.CTkButton(btn_frame, text=bdef["label"],
                                  fg_color=color_code,
                                  command=lambda bd=bdef: self.handle_button(bd))
                b.pack(side="left", padx=3, pady=3)
        else:
            ctk.CTkLabel(self, text="No definition for this objection.").pack(pady=20)

    def handle_button(self, bdef):
        fn = bdef["function"]
        param = bdef.get("param")

        # The function strings often look like: showPopup('xxx'), nextPage(), endCallProcess(), etc.
        if "showPopup(" in fn:
            # e.g. showPopup('noTime')
            inner_id = re.findall(r"showPopup\('([^']+)'\)", fn)
            if inner_id:
                ObjectionPopup(self.master, inner_id[0], self.main_gui)
            self.destroy()

        elif fn == "triggerEndCallProcess()":
            CallDispositionPopup(self.master, self.main_gui)
            self.destroy()

        elif "triggerEndCallAndSetDisposition" in fn:
            # e.g. triggerEndCallAndSetDisposition('NQ-Roof Age')
            disp = re.findall(r"triggerEndCallAndSetDisposition\('([^']+)'\)", fn)
            if disp:
                logger.info(f"Setting disposition to: {disp[0]}")
                cdp = CallDispositionPopup(self.master, self.main_gui)
                cdp.disp_var.set(disp[0])
            self.destroy()

        elif fn == "nextPage()":
            self.main_gui.go_next()
            self.destroy()

        elif fn == "prevPage()":
            self.main_gui.go_previous()
            self.destroy()

        elif fn == "closePopup()":
            self.destroy()

        elif "handleReferralInfoNow" in fn or "handleReferralResponse" in fn:
            tkmsg.showinfo("Referral Info", "Placeholder: not implemented.")
            self.destroy()

        elif "handleNoInsuranceKeepInfo" in fn:
            tkmsg.showinfo("No Insurance Info", "Placeholder: not implemented.")
            self.destroy()

        elif "handleCallBackRequest" in fn:
            tkmsg.showinfo("Call Back Request", "Placeholder: not implemented.")
            self.destroy()

        elif "handleGetLandlordInfo" in fn:
            tkmsg.showinfo("Get Landlord Info", "Placeholder: not implemented.")
            self.destroy()

        elif "showPreviousObjectionPopup()" in fn:
            tkmsg.showinfo("Previous Objection", "Placeholder: not implemented.")
            self.destroy()

        elif fn == "startScript":
            self.main_gui.display_script_page(1)
            self.destroy()

        elif fn == "endCallProcess":
            self.main_gui.confirm_end_call()
            self.destroy()

        else:
            tkmsg.showinfo("Action", f"Unhandled function: {fn}")
            self.destroy()


# -------------------------------------------------------------------------
# RUN APPLICATION
# -------------------------------------------------------------------------
def run_app():
    """
    A single mainloop approach:
      1) Create one hidden root window (ctk.CTk()).
      2) Show a splash window (CTkToplevel).
      3) Then show the login window (CTkToplevel).
      4) Then show the main Storm911App (CTkToplevel).
    All are children of the same root, with only one mainloop.
    """
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.withdraw()

    # Create the login window, but keep it hidden for now
    login_window = LoginScreen(root)
    login_window.withdraw()

    # Create the splash screen, which will un-hide login after 1.5s
    splash = SplashScreen(root, login_window)
    splash.lift()

    # Start the single mainloop
    root.mainloop()


# -------------------------------------------------------------------------
# MAIN ENTRY POINT
# -------------------------------------------------------------------------
if __name__ == "__main__":
    run_app()
