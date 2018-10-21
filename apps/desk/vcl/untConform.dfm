object frmConform: TfrmConform
  Left = 0
  Top = 0
  BorderStyle = bsToolWindow
  Caption = 'Conform'
  ClientHeight = 287
  ClientWidth = 621
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  KeyPreview = True
  OldCreateOrder = False
  Position = poScreenCenter
  OnKeyPress = FormKeyPress
  OnShow = FormShow
  PixelsPerInch = 96
  TextHeight = 13
  object cxLabel2: TcxLabel
    Left = 23
    Top = 151
    Caption = 'Data set Path'
    ParentFont = False
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = []
    Style.IsFontAssigned = True
    Transparent = True
  end
  object cxLabel3: TcxLabel
    Left = 23
    Top = 7
    Caption = 'Latitude Tolerance (+/- deg)'
    ParentFont = False
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = []
    Style.IsFontAssigned = True
    Transparent = True
  end
  object edtLatMargin: TcxTextEdit
    Left = 23
    Top = 33
    BeepOnEnter = False
    ParentFont = False
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = []
    Style.IsFontAssigned = True
    TabOrder = 2
    Text = '0.3'
    Width = 167
  end
  object cxLabel1: TcxLabel
    Left = 223
    Top = 7
    Caption = 'Latitude Tolerance (+/- deg)'
    ParentFont = False
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = []
    Style.IsFontAssigned = True
    Transparent = True
  end
  object edtLonMargin: TcxTextEdit
    Left = 223
    Top = 33
    BeepOnEnter = False
    ParentFont = False
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = []
    Style.IsFontAssigned = True
    TabOrder = 4
    Text = '0.3'
    Width = 167
  end
  object cxLabel4: TcxLabel
    Left = 423
    Top = 7
    Caption = 'Latitude Tolerance (+/- m)'
    ParentFont = False
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = []
    Style.IsFontAssigned = True
    Transparent = True
  end
  object edtDepthMargin: TcxTextEdit
    Left = 423
    Top = 33
    BeepOnEnter = False
    ParentFont = False
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = []
    Style.IsFontAssigned = True
    TabOrder = 6
    Text = '5'
    Width = 167
  end
  object cxLabel5: TcxLabel
    Left = 23
    Top = 79
    Caption = 'Temporal Tolerance (+/- day)'
    ParentFont = False
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = []
    Style.IsFontAssigned = True
    Transparent = True
  end
  object btnColocalize: TcxButton
    Left = 23
    Top = 228
    Width = 567
    Height = 33
    Caption = 'Conform'
    TabOrder = 8
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -13
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
    OnClick = btnColocalizeClick
  end
  object edtTemporalMargin: TcxTextEdit
    Left = 23
    Top = 105
    BeepOnEnter = False
    ParentFont = False
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = []
    Style.IsFontAssigned = True
    TabOrder = 9
    Text = '3'
    Width = 567
  end
  object bedtDatasetConform: TcxButtonEdit
    Left = 23
    Top = 177
    BeepOnEnter = False
    ParentFont = False
    Properties.Buttons = <
      item
        Action = Action1
        Default = True
        Kind = bkEllipsis
      end>
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = []
    Style.IsFontAssigned = True
    TabOrder = 10
    Width = 567
  end
  object aiBusy: TdxActivityIndicator
    Left = 258
    Top = 105
    Width = 121
    Height = 95
    PropertiesClassName = 'TdxActivityIndicatorGravityDotsProperties'
    Transparent = True
    Visible = False
  end
  object OpenDialog1: TOpenDialog
    Filter = 'CSV File|*.csv|Excel File|*.xlsx'
    Left = 519
    Top = 128
  end
  object ActionList1: TActionList
    Left = 559
    Top = 128
    object Action1: TAction
      Caption = 'Action1'
      OnExecute = Action1Execute
    end
  end
end
