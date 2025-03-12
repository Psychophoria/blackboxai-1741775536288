"""
Appointment GUI module for Storm911.
Handles the appointment scheduling interface.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
from datetime import datetime, timedelta
import calendar
from typing import Dict, Callable, Optional

from config import COLORS, TITLE_FONT, HEADER_FONT, NORMAL_FONT, APP_SETTINGS

class AppointmentWindow(ctk.CTkToplevel):
    """Appointment scheduling window."""
    
    def __init__(self, parent, callback: Optional[Callable] = None):
        super().__init__(parent)
        self.callback = callback
        
        self.title("Schedule Appointment")
        self.geometry("800x600")
        self.configure(fg_color=COLORS["light_grey"])
        
        # Make window modal
        self.grab_set()
        
        # Center window on parent
        self.center_window()
        
        # Initialize variables
        self.selected_date = datetime.now()
        self.selected_time = None
        
        # Build UI
        self.create_ui()
        
        # Load initial data
        self.load_availability()

    def center_window(self):
        """Center the window on the parent."""
        self.update_idletasks()
        parent_x = self.master.winfo_x()
        parent_y = self.master.winfo_y()
        parent_width = self.master.winfo_width()
        parent_height = self.master.winfo_height()
        
        width = 800
        height = 600
        
        x = parent_x + (parent_width - width) // 2
        y = parent_y + (parent_height - height) // 2
        
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_ui(self):
        """Create the appointment scheduling interface."""
        # Title
        title = ctk.CTkLabel(
            self,
            text="Schedule Appointment",
            font=TITLE_FONT,
            text_color=COLORS["primary_blue"]
        )
        title.pack(pady=10)
        
        # Main content frame
        content = ctk.CTkFrame(self)
        content.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Split into left and right panels
        content.grid_columnconfigure(0, weight=1)
        content.grid_columnconfigure(1, weight=1)
        
        # Left panel - Calendar
        left_panel = ctk.CTkFrame(content)
        left_panel.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        self.create_calendar(left_panel)
        
        # Right panel - Time slots
        right_panel = ctk.CTkFrame(content)
        right_panel.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        
        self.create_time_slots(right_panel)
        
        # Bottom buttons
        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(fill="x", padx=10, pady=10)
        
        schedule_btn = ctk.CTkButton(
            btn_frame,
            text="Schedule",
            command=self.schedule_appointment,
            fg_color=COLORS["success_green"]
        )
        schedule_btn.pack(side="left", padx=5)
        
        cancel_btn = ctk.CTkButton(
            btn_frame,
            text="Cancel",
            command=self.destroy,
            fg_color=COLORS["error_red"]
        )
        cancel_btn.pack(side="right", padx=5)

    def create_calendar(self, parent):
        """Create the calendar widget."""
        # Month navigation
        nav_frame = ctk.CTkFrame(parent)
        nav_frame.pack(fill="x", pady=5)
        
        prev_btn = ctk.CTkButton(
            nav_frame,
            text="←",
            width=30,
            command=self.previous_month
        )
        prev_btn.pack(side="left", padx=5)
        
        self.month_label = ctk.CTkLabel(
            nav_frame,
            text=self.selected_date.strftime("%B %Y"),
            font=HEADER_FONT
        )
        self.month_label.pack(side="left", expand=True)
        
        next_btn = ctk.CTkButton(
            nav_frame,
            text="→",
            width=30,
            command=self.next_month
        )
        next_btn.pack(side="right", padx=5)
        
        # Calendar grid
        self.calendar_frame = ctk.CTkFrame(parent)
        self.calendar_frame.pack(expand=True, fill="both", padx=5, pady=5)
        
        self.create_calendar_grid()

    def create_calendar_grid(self):
        """Create the calendar day grid."""
        # Clear existing calendar
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()
        
        # Add day headers
        days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for i, day in enumerate(days):
            lbl = ctk.CTkLabel(
                self.calendar_frame,
                text=day,
                font=NORMAL_FONT
            )
            lbl.grid(row=0, column=i, padx=2, pady=2)
        
        # Get calendar for current month
        cal = calendar.monthcalendar(
            self.selected_date.year,
            self.selected_date.month
        )
        
        # Add day buttons
        today = datetime.now().date()
        current_month = self.selected_date.replace(day=1)
        
        for week_num, week in enumerate(cal):
            for day_num, day in enumerate(week):
                if day != 0:
                    date = current_month.replace(day=day).date()
                    
                    # Determine button style
                    if date < today:
                        state = "disabled"
                        color = COLORS["neutral_grey"]
                    else:
                        state = "normal"
                        color = COLORS["primary_blue"]
                    
                    if date == self.selected_date.date():
                        color = COLORS["success_green"]
                    
                    btn = ctk.CTkButton(
                        self.calendar_frame,
                        text=str(day),
                        width=30,
                        height=30,
                        fg_color=color,
                        state=state,
                        command=lambda d=date: self.select_date(d)
                    )
                    btn.grid(
                        row=week_num + 1,
                        column=day_num,
                        padx=2,
                        pady=2
                    )

    def create_time_slots(self, parent):
        """Create the time slots panel."""
        # Title
        title = ctk.CTkLabel(
            parent,
            text="Available Times",
            font=HEADER_FONT
        )
        title.pack(pady=5)
        
        # Time slots container
        self.time_frame = ctk.CTkFrame(parent)
        self.time_frame.pack(expand=True, fill="both", padx=5, pady=5)
        
        # Will be populated by load_availability()

    def load_availability(self):
        """Load available time slots for selected date."""
        # Clear existing time slots
        for widget in self.time_frame.winfo_children():
            widget.destroy()
        
        # Example time slots (9 AM to 5 PM)
        start_hour = 9
        end_hour = 17
        
        for hour in range(start_hour, end_hour):
            for minute in [0, 30]:
                time_str = f"{hour:02d}:{minute:02d}"
                
                # Example: Randomly make some slots unavailable
                import random
                available = random.choice([True, True, True, False])
                
                if available:
                    color = COLORS["primary_blue"]
                    state = "normal"
                else:
                    color = COLORS["neutral_grey"]
                    state = "disabled"
                
                # If this is the selected time, highlight it
                if self.selected_time == time_str:
                    color = COLORS["success_green"]
                
                btn = ctk.CTkButton(
                    self.time_frame,
                    text=time_str,
                    fg_color=color,
                    state=state,
                    command=lambda t=time_str: self.select_time(t)
                )
                btn.pack(fill="x", padx=5, pady=2)

    def previous_month(self):
        """Go to previous month."""
        self.selected_date = self.selected_date.replace(day=1) - timedelta(days=1)
        self.month_label.configure(
            text=self.selected_date.strftime("%B %Y")
        )
        self.create_calendar_grid()

    def next_month(self):
        """Go to next month."""
        self.selected_date = (
            self.selected_date.replace(day=1) + 
            timedelta(days=32)
        ).replace(day=1)
        self.month_label.configure(
            text=self.selected_date.strftime("%B %Y")
        )
        self.create_calendar_grid()

    def select_date(self, date):
        """Handle date selection."""
        self.selected_date = datetime.combine(date, datetime.min.time())
        self.create_calendar_grid()
        self.load_availability()

    def select_time(self, time_str):
        """Handle time slot selection."""
        self.selected_time = time_str
        self.load_availability()

    def schedule_appointment(self):
        """Handle appointment scheduling."""
        if not self.selected_time:
            messagebox.showwarning(
                "Warning",
                "Please select an appointment time."
            )
            return
        
        # Format the appointment datetime
        hour, minute = map(int, self.selected_time.split(":"))
        appointment_datetime = self.selected_date.replace(
            hour=hour,
            minute=minute
        )
        
        # Create appointment data
        appointment_data = {
            "datetime": appointment_datetime.isoformat(),
            "status": "scheduled"
        }
        
        # Notify callback if provided
        if self.callback:
            self.callback(appointment_data)
        
        messagebox.showinfo(
            "Success",
            f"Appointment scheduled for {appointment_datetime.strftime('%B %d, %Y at %I:%M %p')}"
        )
        
        self.destroy()

if __name__ == "__main__":
    # Test the appointment window
    root = ctk.CTk()
    root.withdraw()
    
    def on_appointment(data):
        print(f"Appointment scheduled: {data}")
    
    app = AppointmentWindow(root, callback=on_appointment)
    root.mainloop()
