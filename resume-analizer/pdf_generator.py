from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from datetime import datetime
import io

def generate_pdf_report(result, resume_name, username="Guest"):
    buffer = io.BytesIO()
    # Margins: 0.5 inch (36 points) for maximum space but professional look
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    story = []
    styles = getSampleStyleSheet()
    
    # Define custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=colors.HexColor('#0F172A'),  # Slate-900
        spaceAfter=15
    )
    
    section_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#1E3A8A'),  # Dark Blue
        spaceBefore=18,
        spaceAfter=8
    )
    
    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#334155')  # Slate-700
    )
    
    bold_body_style = ParagraphStyle(
        'BoldBodyTextCustom',
        parent=body_style,
        fontName='Helvetica-Bold'
    )
    
    # Title
    story.append(Paragraph("AI Resume Analysis Report", title_style))
    story.append(Spacer(1, 10))
    
    # Info metadata block
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    score = result['score']
    
    # Set status badge color based on score
    score_color = '#10B981' if score >= 80 else ('#F59E0B' if score >= 60 else '#EF4444')
    
    meta_data = [
        [Paragraph("Candidate:", bold_body_style), Paragraph(username, body_style)],
        [Paragraph("Resume File:", bold_body_style), Paragraph(resume_name, body_style)],
        [Paragraph("Date Analyzed:", bold_body_style), Paragraph(date_str, body_style)],
        [
            Paragraph("ATS Match Score:", bold_body_style),
            Paragraph(f"<font color='{score_color}'><b>{score}%</b></font>", bold_body_style)
        ]
    ]
    
    # Column width: label=120, info=420 (sum = 540, which fits 612 - 72 width of margins)
    meta_table = Table(meta_data, colWidths=[130, 410])
    meta_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BACKGROUND', (0,3), (1,3), colors.HexColor('#F8FAFC')), # light background for score row
        ('LINEBELOW', (0,0), (-1,-2), 0.5, colors.HexColor('#E2E8F0')),
        ('LINEBELOW', (0,3), (-1,3), 1, colors.HexColor(score_color)),
    ]))
    
    story.append(meta_table)
    story.append(Spacer(1, 15))
    
    # Matched Skills Section
    story.append(Paragraph("Matched Skills", section_style))
    matched_skills = result['matched']
    if matched_skills:
        # Wrap skills in custom styled box or table
        skills_para = [Paragraph(skill, body_style) for skill in matched_skills]
        # Group skills in a neat display format
        skills_text = ", ".join(matched_skills)
        story.append(Paragraph(skills_text, body_style))
    else:
        story.append(Paragraph("No matching skills found in the resume for the target job description.", body_style))
    
    # Missing Skills Section
    story.append(Paragraph("Missing Skills", section_style))
    missing_skills = result['missing']
    if missing_skills:
        skills_text = ", ".join(missing_skills)
        story.append(Paragraph(skills_text, body_style))
    else:
        story.append(Paragraph("Excellent! The resume matches all the required skills from the job description.", body_style))
        
    # Suggestions Section
    story.append(Paragraph("Recommendations & Suggestions", section_style))
    suggestions = result['suggestions']
    if suggestions:
        for suggestion in suggestions:
            story.append(Paragraph(f"• {suggestion}", body_style))
            story.append(Spacer(1, 4))
    else:
        story.append(Paragraph("No additional changes required.", body_style))
        
    # Build Document
    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()
