function oscheck() {
	$CurrentBuild = Get-ItemPropertyValue 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion' -Name CurrentBuild
	if ($CurrentBuild -lt 19044) {
		return $false
	}
	elseif ($CurrentBuild -ge 19044) {
		return $true
	}
}

function isadmin() {
	$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
	$admin = $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
	return $admin
}

function isonline() {
	Import-Module BitsTransfer
	Start-BitsTransfer "https://raw.githubusercontent.com/WinRice/Files/main/File.txt"
	if (Test-Path File.txt) {
		Remove-Item File.txt
		return $true
	}
	elseif (!(Test-Path File.txt)) {
		return $false | Out-Null
	}
}

function isrestartpending() {
	param (
		[Parameter(
			Mandatory = $false,
			ValueFromPipeline = $true,
			ValueFromPipelineByPropertyName = $true,
			Position = 0
		)]
		[string[]]  $ComputerName = $env:COMPUTERNAME
	)
	ForEach ($Computer in $ComputerName) {
		$PendingReboot = $false
		$HKLM = [UInt32] "0x80000002"
		$WMI_Reg = [WMIClass] "\\$Computer\root\default:StdRegProv"
		if ($WMI_Reg) {
			if (($WMI_Reg.EnumKey($HKLM, "SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\")).sNames -contains 'RebootPending') { $PendingReboot = $true }
			if (($WMI_Reg.EnumKey($HKLM, "SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\")).sNames -contains 'RebootRequired') { $PendingReboot = $true }
		
			# Check for SCCM namespace.
			$SCCM_Namespace = Get-WmiObject -Namespace ROOT\CCM\ClientSDK -List -ComputerName $Computer -ErrorAction Ignore
			if ($SCCM_Namespace) {
				if (([WmiClass]"\\$Computer\ROOT\CCM\ClientSDK:CCM_ClientUtilities").DetermineIfRebootPending().RebootPending -eq $true) { $PendingReboot = $true }
			}
		
			if ($PendingReboot -eq $true) {
				return $false
			}
			else {
				return $true
			}
		}   
	}
}
